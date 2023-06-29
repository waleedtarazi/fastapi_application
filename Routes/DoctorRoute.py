from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from db.database import get_db_connection
from Models.UserModel import DoctorUser
from Models.DoctorModel import *
from Services.DoctorService.doctorService import(Sign_Up, 
                                                 Log_In, 
                                                 Get_Profile, 
                                                 Edit_Profile, 
                                                 Get_Patients) 
# Router
DoctorRouter = APIRouter(prefix="/doctor", tags=["Doctor"])

# Index
@DoctorRouter.get("/")
def index():
    raise HTTPException(status_code=404, detail= "no root for this directory for now, please visit us again")

# Sign up
@DoctorRouter.post("/signup", tags=['Doctor'])
async def sign_up(doctor: DoctorCreate, db: Session = Depends(get_db_connection)):
    return await Sign_Up(doctor, db)
    
# Log In
@DoctorRouter.post('/signin', tags=['Doctor'])
async def login(doctor: DoctorLogIn, db: Session = Depends(get_db_connection)):
    return await Log_In(doctor, db)
    
# Get Profile
@DoctorRouter.get('/profile', response_model=Doctor, tags=['Doctor'])
async def get_profile(doctor_token: str = Header(None), db: Session = Depends(get_db_connection)):
    return await Get_Profile(doctor_token, db)
    
# Edite Profile 
@DoctorRouter.put('/profile', response_model=Doctor, tags=['Doctor'])
async def edit_profile(doctor_update: DoctorUpdate, doctor_token: str = Header(None), db: Session = Depends(get_db_connection)):
    return await Edit_Profile(doctor_update, doctor_token, db)

# Get doctor's patients
@DoctorRouter.get('/patients', response_model=list[DoctorUser], tags=['Doctor'])
async def get_patients(doctor_token: str = Header(None), db: Session = Depends(get_db_connection)):
    return await Get_Patients(doctor_token, db)

# Get Appoitments
