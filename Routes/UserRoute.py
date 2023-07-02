from typing import Union
from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from Services.UserService.SendRequest import make_request_with_doctor, make_request_with_doctor_test
from Services.UserService.userService import *
from db.database import get_db_connection
from Models.UserModel import *
from Models.FeelingModel import Feeling
from Models.RequestModel import UserAddRequst
from Services.auth.auth import Sign_Up_client, Log_In_client, Edit_Profile_client, Get_Profile_client
from Schemas.UserSchema import User as SchemaUser


UserRouter = APIRouter(prefix="/user", tags=["User"])
type_ = SchemaUser

@UserRouter.get("/")
def index():
    raise HTTPException(status_code=404, detail= "no root for this directory for now, please visit us again")

#* Sign up
@UserRouter.post("/signup", tags=['User'])
async def sign_up(user: UserCreate, db: Session = Depends(get_db_connection)):
    return await Sign_Up_client(client= user, db= db)
    
#* Log In
@UserRouter.post('/signin', tags=['User'])
async def login(user: UserLogIn, db: Session = Depends(get_db_connection)):
    return await Log_In_client(client= user, db=db, type_= type_) 
    
#* Get Profile
@UserRouter.get('/profile', response_model=UserProfile, tags=['User'])
async def get_profile(user_token: str = Header(None), db: Session = Depends(get_db_connection)):
    return await Get_Profile_client(user_token, db, type_)
    
#* Edite Profile 
@UserRouter.put('/profile', tags=['User'])
async def edit_profile(user_update: UserUpdate, user_token: str = Header(None), db: Session = Depends(get_db_connection)):
    return await Edit_Profile_client(user_update, user_token, db, type_)
        
#* GET Feelings 
@UserRouter.get('/feelings', response_model= list[Feeling], tags=['User'])
async def get_feelings(month:Union[int, None] = None,
                       year:Union[int, None] = None,
                       user_token:str= Header(None),
                       db: Session = Depends(get_db_connection)):
    return await Get_Feelings(month, year, user_token, db)

#* Make appoitment with doctor        
@UserRouter.post('/request_doctor', tags=['User'])
async def make_doctor_request(doctor_id: int, user_token: str = Header(None), db: Session = Depends(get_db_connection)):
    request_db = make_request_with_doctor(user_token, doctor_id, db)
    if request_db:
        return {"request": request_db}   
    

@UserRouter.post('/test_request_doctor', tags=['User'])
async def make_doctor_request_test(user_id:int, doctor_id: int, db: Session = Depends(get_db_connection)):
    request_db = make_request_with_doctor_test(user_id, doctor_id, db)
    if request_db:
        return {"request": request_db}
        # raise HTTPException(status_code=400, detail= "Request couldn't be created")
