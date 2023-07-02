from sqlalchemy.orm import Session
from fastapi import HTTPException
from JWT.jwt_handler import get_JWT_ID
from Models.DoctorModel import Doctor
from Models.RequestModel import UserAddRequst
from Repository.DoctorRepository import get_a_request_db, get_all_requests_db
from Repository.RequestRepository import create_request_db, update_request_db
from Repository.auth import get_client_db
from Schemas.UserSchema import User as SchemaUser
from Schemas.DoctorSchema import Doctor as SchemaDoctor
from Schemas.RequestSchema import Request as SchemaRequest, RequestStatus
from Models.RequestModel import RequestInformation


def update_request_status(request: SchemaRequest, new_status: str):
        
    if not request:
        raise HTTPException(status_code=404, detail="Request not found")
    
    if request.status != RequestStatus.PINNING:
        raise HTTPException(status_code=400, detail="Request already responded")

    if new_status == "accepted":
        request.status = RequestStatus.ACCEPTED
        request.doctor.patients.append(request.user)
        
    elif new_status == "denied":
        request.status = RequestStatus.DENIED
        
    return request


async def respons_to_request(doctor_token: str, request_id: int, response: str, db: Session):
    
    doctor_id = get_JWT_ID(doctor_token)
    
    request = get_a_request_db(doctor_id, request_id, db)
    print('the request before updated request',request)
    updated_request = update_request_status(request, response)
    print('the request after updated request',updated_request)
    updated_request_db = update_request_db(updated_request,db)
    print('the request after retrive from db request',update_request_db)
    
    user = updated_request_db.user
    doctor = updated_request_db.doctor
    
    request_info = RequestInformation.from_obj(user,doctor,updated_request_db)
    
    return request_info

async def Get_Requests(doctor_token: str, on_status:str, db: Session):
    """Get the all Requests from the DB and then convert into requestinfo model"""
    doctor_id = get_JWT_ID(doctor_token)
    
    requests = get_all_requests_db(doctor_id, db, on_status)
    requests_info = [RequestInformation.from_obj(request.user, request.doctor, request) for request in requests]

    return requests_info
    
    
    
    