from typing import Union, Optional
from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from auth.jwt_handler import signJWT, get_JWT_ID
from auth.crypto_handler import verify_password
from db.database import get_db_connection
from schemas.UserSchema import *
from services.UserService import *
from services.FeelingService import get_all_feelings, get_monthly_feelings


UserRouter = APIRouter(prefix="/user", tags=["User"])


@UserRouter.get("/")
def index():
    raise HTTPException(status_code=404, detail= "no root for this directory for now, please visit us again")


@UserRouter.post("/signup" , tags=['User'])
async def sign_up(user: UserCreate, db: Session = Depends(get_db_connection)):
    if user.password != user.confirm_password:
        raise HTTPException(status_code = 400, detail= 'Passwords are not matched, please enter matched passwords')
    db_user = get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    created = create_user(db=db, user=user)
    return {'access_token': signJWT(created.id)['access_token'],
             'user': created}

# ------------------- LOGIN -------------
@UserRouter.post('/signin', tags=['User'])
async def login(user: UserLogIn, db: Session= Depends(get_db_connection)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        if verify_password(user.password,db_user.hashed_password):
            return {
                'access_token': signJWT(db_user.id)['access_token'] ,
                'user': db_user
            }
        else:
            raise HTTPException(status_code=400, detail='Invalid password')
    else:
        raise HTTPException(status_code=400, detail='Invalid password')
    

# ------------ GET USER PROFILE -------
@UserRouter.get('/profile',response_model=User, tags=['User'])
async def get_profile(user_token: Union[str, None] = Header(None),db: Session = Depends(get_db_connection)):
    if user_token:
        db_user = get_user(db= db, user_id=get_JWT_ID(user_token))
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return db_user
    else:
        raise HTTPException(status_code=401, detail='No token provided!, please LogIn first')
    
    
    
# ---------------- EDIT USER PROFILE -----------
@UserRouter.put('/profile',response_model= User, tags= ['User'])
async def edit_profile(user_update:UserUpdate,user_token: Union[str,None] = Header(None), db: Session = Depends(get_db_connection)):
    if user_token:
        print(get_JWT_ID(user_token))
        db_user = get_user(db=db,user_id=get_JWT_ID(user_token))
        if db_user:
            return update_user(db = db,user_id= get_JWT_ID(user_token),user_update= user_update)
        else:
            raise HTTPException(status_code=404, detail='No user found' )
    else:
        raise HTTPException(status_code=401, detail="Not Authorized")
        


# -------- GET USER FEELINGS ---------------
# , response_model=list[schemas.Feeling]
@UserRouter.get('/feelings',tags=['User'])
async def get_feelings(month:Union[int, None] = None,
                       year:Union[int, None] = None,
                       user_token:Union[str,None]= Header(None),
                       db: Session = Depends(get_db_connection)):
    if user_token:
        if not (month and year):
            db_feelings = get_all_feelings(user_id=get_JWT_ID(user_token), db=db)
        else:
            db_feelings = get_monthly_feelings(db=db, id=get_JWT_ID(user_token), year=year, month=month)
        return db_feelings
    else:
        raise HTTPException(status_code=401, detail="Not Authorized")


