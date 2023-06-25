from typing import Union
from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from db.database import get_db_connection
from Models.UserModel import *
from Models.FeelingModel import Feeling



from Services.UserService.userService import Sign_Up, Log_In, Get_Profile, Edit_Profile, Get_Feelings

UserRouter = APIRouter(prefix="/user", tags=["User"])
email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

@UserRouter.get("/")
def index():
    raise HTTPException(status_code=404, detail= "no root for this directory for now, please visit us again")

# Sign up
@UserRouter.post("/signup", tags=['User'])
async def sign_up(user: UserCreate, db: Session = Depends(get_db_connection)):
    return await Sign_Up(user, db)
    
# Log In
@UserRouter.post('/signin', tags=['User'])
async def login(user: UserLogIn, db: Session = Depends(get_db_connection)):
    return await Log_In(user, db)
    

# Get Profile
@UserRouter.get('/profile', response_model=User, tags=['User'])
async def get_profile(user_token: str = Header(None), db: Session = Depends(get_db_connection)):
    return await Get_Profile(user_token, db)
    
# Edite Profile 
@UserRouter.put('/profile', response_model=User, tags=['User'])
async def edit_profile(user_update: UserUpdate, user_token: str = Header(None), db: Session = Depends(get_db_connection)):
    return await Edit_Profile(user_update, user_token, db)
        
# GET Feelings 
@UserRouter.get('/feelings', response_model= list[Feeling], tags=['User'])
async def get_feelings(month:Union[int, None] = None,
                       year:Union[int, None] = None,
                       user_token:str= Header(None),
                       db: Session = Depends(get_db_connection)):
    return await Get_Feelings(month, year, user_token, db)