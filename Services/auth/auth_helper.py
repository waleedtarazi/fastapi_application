from typing import Dict, Type, Union
from sqlalchemy.orm import Session
from fastapi import HTTPException
from JWT.crypto_handler import get_password_hash, verify_password
from JWT.jwt_handler import  signJWT
from Models.DoctorModel import DoctorCreate,  DoctorProfile, DoctorUpdate
from Models.UserModel import UserCreate, UserProfile, UserUpdate
from Repository.ActivityRepository import get_activities
from Repository.UserRepository import get_user_by_email, update_user_db
from Repository.auth import create_client_db, get_client_by_email, update_client_db
from Schemas.DoctorSchema import Doctor as SchemaDoctor
from Schemas.UserSchema import User as SchemaUser
 
    
async def create_clinet(db: Session, client: Union[UserCreate, DoctorCreate], type_: Union[Type[SchemaUser], Type[SchemaDoctor]]) -> Union[str, UserProfile, DoctorProfile]:
    db_obj = get_client_by_email(db, client.email, type_)
    if db_obj:
        raise HTTPException(status_code=400, detail='Email already registered.')
    
    created_obj = create_client_db(db=db, client= client, client_type=type_)
    access_token = signJWT(created_obj.id)['access_token']
    if type_ == SchemaDoctor:
        created_profile = DoctorProfile.from_obj(created_obj)
    else:
        created_profile = UserProfile.from_obj(created_obj)
        user =  get_user_by_email(db, created_profile.email)
        activites =  get_activities(db)
        user.activities = activites 
        _ = update_user_db(user, db)
    return access_token, created_profile


def convert_schema_profile(client: Union[SchemaUser, SchemaDoctor]) -> Union[UserProfile, DoctorProfile]:
    """check the client type"""
    if isinstance(client, SchemaUser):
        client_profile = UserProfile.from_obj(client)
    elif isinstance(client, SchemaDoctor):
        client_profile = DoctorProfile.from_obj(client)
    else:
        raise HTTPException(status_code=400, detail=f"Invalid Account type: {type(client)}")
    
    return client_profile


def update_password(update_dic: dict, old_password:str):
    if update_dic['current_password']:
        if not update_dic['new_password']:
            raise HTTPException(status_code=400, detail='New password not provided')
        if not update_dic['confirm_new_password']:
            raise HTTPException(status_code=400, detail='Confirm new password not provided')
        if not verify_password(update_dic['current_password'], old_password):
            raise HTTPException(status_code=400, detail='Current password not correct')
        if not update_dic['new_password'] == update_dic['confirm_new_password']:
            raise HTTPException(status_code=400, detail='Passwords do not match. Please enter matching passwords.')
        else:
            return True, get_password_hash(update_dic['new_password'])
    return False,''

def update_client(client_update: Union[UserUpdate, DoctorUpdate], old_client:Union[SchemaUser, SchemaDoctor], db: Session):
   
    client_update_dict = {**vars(client_update)}
    status, new_password = update_password(client_update_dict, old_client.hashed_password)
    if status:
        client_update_dict['hashed_password'] = new_password    
    for key, value in client_update_dict.items():
        if hasattr(old_client, key) and value not in (None, 0, 'None', " ", ""): 
            if getattr(old_client, key) != value:
                setattr(old_client, key, value)
    updated_client = update_client_db(old_client,db)
    updated_client = convert_schema_profile(updated_client)
    
    return updated_client