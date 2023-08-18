from typing import Union
from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from Services.UserService.RequestServices import get_user_requests, make_request_with_doctor
from Services.UserService.userService import *
from db.database import get_db_connection
from Models.UserModel import *
from Models.FeelingModel import Feeling
from Models.ActivityModel import Activity
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
@UserRouter.get('/feelings', tags=['User'])
async def get_feelings(month:Union[int, None] = None,
                       year:Union[int, None] = None,
                       user_token:str= Header(None),
                       db: Session = Depends(get_db_connection)):
    feelings = await Get_Feelings(month, year, user_token, db)
    if feelings:
        return feelings
    else:
        raise HTTPException(status_code=200, detail = "لا يوجد مشاعر كافية لعرضها")

#* make feeling
@UserRouter.post('/feelings', tags=['User'])
async def make_feeling(new_feeling: FeelingCreate, user_token: str = Header(None), db: Session = Depends(get_db_connection)):
    return await Add_Feeling(new_feeling,user_token,db)
    

#* Make appoitment with doctor        
@UserRouter.post('/request_doctor', tags=['User'])
async def make_doctor_request(doctor_id: int, desctiption:str, user_token: str = Header(None), db: Session = Depends(get_db_connection)):
    request_db = make_request_with_doctor(user_token, doctor_id, desctiption, db)
    if request_db:
        return {"request": request_db}

#* get user requests
@UserRouter.get('/requests', tags=['User'])
async def get_request(user_token: str = Header(None), db: Session = Depends(get_db_connection)):
    return await get_user_requests(user_token,db)

#* Get Activities
@UserRouter.get('/activity', tags=['User'])
async def get_activities(user_token: str = Header(None), db: Session = Depends(get_db_connection)):
    return await Get_Activites(user_token, db)

#* Update Activity weight value 
@UserRouter.put('/activity', tags=["User"])
async def update_activity(added_weight: int, activity_id: int, user_token: str = Header(None), db: Session = Depends(get_db_connection)):
    updated_activity = await Update_Activity_Weight(user_token=user_token, activity_id=activity_id, added_weight=added_weight, db=db)
    return updated_activity