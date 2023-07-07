from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from db.database import get_db_connection
from Models.UserModel import DoctorUser
from Models.DoctorModel import *
from Services.DoctorService.doctorService import Get_Patients
from Services.DoctorService.HandleRequests import respons_to_request, Get_Requests
from Schemas.RequestSchema import RequestStatus
from Services.auth.auth import Sign_Up_client, Log_In_client, Edit_Profile_client, Get_Profile_client
from Schemas.DoctorSchema import Doctor as ShemaDoctor
# Router
DoctorRouter = APIRouter(prefix="/doctor", tags=["Doctor"])

type_ = ShemaDoctor
# Index
@DoctorRouter.get("/")
def index():
    raise HTTPException(status_code=404, detail= "no root for this directory for now, please visit us again")

#* Sign up
@DoctorRouter.post("/signup", tags=['Doctor'])
async def sign_up(doctor: DoctorCreate, db: Session = Depends(get_db_connection)):
    return await Sign_Up_client(doctor, db)
    
#* Log In
@DoctorRouter.post('/signin', tags=['Doctor'])
async def login(doctor: DoctorLogIn, db: Session = Depends(get_db_connection)):
    return await Log_In_client(client= doctor, db=db, type_=type_ )
    
#* Get Profile
@DoctorRouter.get('/profile', tags=['Doctor'])
async def get_profile(doctor_token: str = Header(None), db: Session = Depends(get_db_connection)):
    return await Get_Profile_client(doctor_token, db, type_)
    
#* Edite Profile 
@DoctorRouter.put('/profile', tags=['Doctor'])
async def edit_profile(doctor_update: DoctorUpdate, doctor_token: str = Header(None), db: Session = Depends(get_db_connection)):
    return await Edit_Profile_client(doctor_update, doctor_token, db, type_)

#* Get doctor's patients
@DoctorRouter.get('/patients', response_model=list[DoctorUser], tags=['Doctor'])
async def get_patients(doctor_token: str = Header(None), db: Session = Depends(get_db_connection)):
    return await Get_Patients(doctor_token, db)

#* update request status
@DoctorRouter.put("/update_request", tags=['Doctor'])
async def update_request(doctor_response: RequestStatus , request_id: int, doctor_token: str = Header(None), db: Session = Depends(get_db_connection)):
    #! send notification to user informing him about the state of the request
    updated_request = await respons_to_request(doctor_token,request_id, doctor_response, db)
    return updated_request

#* Get all requests 
@DoctorRouter.get("/my_requests", tags=['Doctor'])
async def get_requests(doctor_token: str = Header(None), on_status:Optional[str] = 'all', db: Session = Depends(get_db_connection)):
    updated_request = await Get_Requests(doctor_token, on_status, db)
    return updated_request
