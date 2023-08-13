import re
from typing import Dict, Union
from sqlalchemy.orm import Session
from fastapi import HTTPException
from JWT.crypto_handler import verify_password
from JWT.jwt_handler import get_JWT_ID, signJWT
from Models.DoctorModel import DoctorCreate, DoctorLogIn, DoctorProfile, DoctorUpdate
from Models.UserModel import UserCreate, UserLogIn, UserProfile, UserUpdate
from Repository.auth import get_client_by_email, get_client_db
from Schemas.DoctorSchema import Doctor as SchemaDoctor
from Schemas.UserSchema import User as SchemaUser
from .auth_helper import create_clinet, convert_schema_profile, update_client


async def Sign_Up_client(client: Union[UserCreate,DoctorCreate], db: Session) -> Dict[str, Union[str, UserProfile, DoctorProfile]]:
    """ SignUp Client(user/doctor) """
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, client.email):
        raise HTTPException(status_code=400, detail='Invalid email address')
    if client.password != client.confirm_password:
        raise HTTPException(status_code=400, detail='Passwords do not match. Please enter matching passwords.')
    
    if isinstance(client, UserCreate):
        access_token, created_profile = await create_clinet(db, client, SchemaUser)
    elif isinstance(client, DoctorCreate):
        access_token, created_profile = await create_clinet(db, client, SchemaDoctor)
    else:
        raise HTTPException(status_code=400, detail=f"Invalid Account type: {type(client)}")

    return {'access_token': access_token, 'client': created_profile}
            

async def Log_In_client(client: Union[UserLogIn,DoctorLogIn], db: Session, type_ = Union[SchemaUser, SchemaDoctor]) -> Dict[str, Union[str, UserProfile, DoctorProfile]]:
    """ LogIn Client(user/doctor) """
    db_client = get_client_by_email(db, client.email, type_)
    if db_client is None or not verify_password(client.password, db_client.hashed_password):
        raise HTTPException(status_code=400, detail='Invalid email or password.')
    
    access_token = signJWT(db_client.id)['access_token']
    
    db_client = convert_schema_profile(db_client)    
    return {'access_token': access_token, 'client': db_client}
    

async def Get_Profile_client(client_token: str, db: Session, type_ = Union[SchemaUser, SchemaDoctor])-> Union[UserProfile, DoctorProfile]:
    """Get Client(user/doctor) Pofile"""
    if not client_token:
        raise HTTPException(status_code=401, detail='No token provided. Please log in first.')
    db_client = get_client_db(db, get_JWT_ID(client_token),type_)
    if not db_client:
        raise HTTPException(status_code=404, detail='Account not found.')
    
    db_client = convert_schema_profile(db_client)    
    return db_client 


async def Edit_Profile_client(client_update: Union[UserUpdate, DoctorUpdate], client_token, db, type_ = Union[SchemaUser, SchemaDoctor]) -> Union[UserProfile, DoctorProfile]:
    """ Edit Client(user/doctor) Profile"""
    if not client_token:
        raise HTTPException(status_code=401, detail='Not authorized. Please log in first.')
    
    client_id = get_JWT_ID(client_token)
    db_client = get_client_db(db=db, client_id=client_id, client_type=type_)
    
    if not db_client:
        raise HTTPException(status_code=404, detail='Account not found.')
    
    updated_client = update_client(client_update= client_update, old_client=db_client, db=db) 
    return updated_client

