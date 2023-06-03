from fastapi import Depends, FastAPI, HTTPException, Header, Cookie
from typing import Annotated, List, Union
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from sql_app.auth.jwt_handler import signJWT, get_JWT_ID
from sql_app.auth.jwt_bearer import JWTBearer
from sql_app.auth.crypto_handler import verify_password, get_password_hash
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ------------------ SighUP ------------------
@app.post("/users/signup" , tags=['User'])
async def sign_up(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    created = crud.create_user(db=db, user=user)
    return {'access_token': signJWT(created.id),
             'user': created}

# ------------------- LOGIN -------------
@app.post('/users/login', tags=['User'])
async def login(user: schemas.UserLogIn, db: Session= Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        if verify_password(user.password,db_user.hashed_password):
            return {
                'access_token': signJWT(db_user.id) ,
                'user': db_user
            }
        else:
            return {'Error': 'Invalid password'}
    else:
        return {'Error': 'invalid email'}
    

# ------------ GET USER PROFILE -------
@app.get('/profile',tags=['User'], response_model=schemas.User)
async def get_profile(user_token: Union[str, None] = Header(None),db: Session = Depends(get_db)):
    print(user_token)
    print(get_JWT_ID(user_token))
    if user_token:
        db_user = crud.get_user(db= db, user_id=get_JWT_ID(user_token))
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return db_user
    else:
        raise HTTPException(status_code=400, detail='No token provided!, please LogIn first')



# ------------ ALL USERS ------------
@app.get("/users/", response_model= list[schemas.User],tags=['Dashboard'])
async def read_all_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    print(users[0])
    return users

# ---------- SPECIFIC USER ----------------
@app.get("/users/{user_id}", response_model=schemas.User, tags=['Dashboard'])
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# -------------- Feelings ----------------
@app.get('/feelings/', tags=['Feelings']) 
#TODO detirment the return type
async def get_user_feelings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    feelings = crud.get_all_feelings(db=db, skip=skip, limit=limit)
    return feelings

@app.post('/seed{user_id}',tags=['Feelings'])
async def seeds(user_id:int, db:Session = Depends(get_db)):
        feelings = crud.seeding(db=db, user_id=user_id)
        return {'msg':'seeding complete'}
     



# ------------- ADD ITEM -------------------
@app.post("/users/{user_id}/items/", dependencies=[Depends(JWTBearer())],response_model=schemas.Item, tags=['Dashboard'])
async def create_item_for_user(user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_user_item(db=db, item=item, user_id=user_id)

# ------------- USER'S ITEMS -------------------
@app.get("/users/{user_id}/items/", response_model=list[schemas.Item], tags=['Dashboard'])
async def read_user_items( user_id: int , db: Session = Depends(get_db)):
    items = crud.get_user_items(id= user_id, db= db)
    return items

# --------------- ALL ITEMS -----------------
@app.get("/items/", response_model=list[schemas.Item], tags=['Dashboard'])
async def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
