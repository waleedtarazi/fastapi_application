import re
from typing import Union
from fastapi import Depends, HTTPException, Header
from sqlalchemy.orm import Session
from JWT.jwt_handler import signJWT, get_JWT_ID
from JWT.crypto_handler import verify_password
from db.database import get_db_connection
from Models.UserModel import UserLogIn
from Repository.UserRepository import *
from Repository.FeelingRepository import get_all_feelings, get_monthly_feelings

email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

async def Sign_Up(user: UserCreate, db: Session = Depends(get_db_connection)):
    if not re.match(email_regex, user.email):
        raise HTTPException(status_code=400, detail='Invalid email address')
    if user.password != user.confirm_password:
        raise HTTPException(status_code=400, detail='Passwords do not match. Please enter matching passwords.')
    db_user = get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail='Email already registered.')
    
    created_user = create_user(db, user)
    access_token = signJWT(created_user.id)['access_token']
    return {'access_token': access_token, 'user': created_user}


async def Log_In(user: UserLogIn, db: Session = Depends(get_db_connection)):
    db_user = get_user_by_email(db, user.email)
    if db_user is None or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail='Invalid email or password.')
    
    access_token = signJWT(db_user.id)['access_token']
    return {'access_token': access_token, 'user': db_user}



async def Get_Profile(user_token: str = Header(None), db: Session = Depends(get_db_connection)):
    if not user_token:
        raise HTTPException(status_code=401, detail='No token provided. Please log in first.')
    
    db_user = get_user(db, get_JWT_ID(user_token))
    if not db_user:
        raise HTTPException(status_code=404, detail='User not found.')
    
    return db_user


async def Edit_Profile(user_update: UserUpdate, user_token: str = Header(None), db: Session = Depends(get_db_connection)):
    if not user_token:
        raise HTTPException(status_code=401, detail='Not authorized. Please log in first.')
    
    user_id = get_JWT_ID(user_token)
    db_user = get_user(db=db, user_id=user_id)
    
    if not db_user:
        raise HTTPException(status_code=404, detail='User not found.')
    
    return update_user(db=db, user_id=user_id, user_update=user_update)



async def Get_Feelings(month:Union[int, None] = None,
                       year:Union[int, None] = None,
                       user_token:str= Header(None),
                       db: Session = Depends(get_db_connection)):
    if not user_token:
        raise HTTPException(status_code=401, detail="Not Authorized")
    if not (month and year):
        db_feelings = get_all_feelings(user_id=get_JWT_ID(user_token), db=db)
    else:
        db_feelings = get_monthly_feelings(db=db, id=get_JWT_ID(user_token), year=year, month=month)
    return db_feelings