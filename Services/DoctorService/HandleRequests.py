from sqlalchemy.orm import Session
from fastapi import HTTPException
from JWT.jwt_handler import get_JWT_ID
from Repository.DoctorRepository import get_a_request_db, get_all_requests_db
from Repository.RequestRepository import update_request_db
from Schemas.RequestSchema import Request as SchemaRequest, RequestStatus
from Models.RequestModel import RequestInformation


def update_request_status(request: SchemaRequest, new_status: RequestStatus):
    """Update the request status"""
    if not request:
        raise HTTPException(status_code=404, detail="Request not found")
    
    if request.status != RequestStatus.PINNING:
        raise HTTPException(status_code=400, detail="Request already responded")

    request.status = new_status
    
    if request.status == RequestStatus.ACCEPTED:
        request.doctor.patients.append(request.user)

    return request


async def respons_to_request(doctor_token: str, request_id: int, response: RequestStatus, db: Session):
    """Response to the request depening on what doctor sent(accept, denied, pinning)"""
    doctor_id = get_JWT_ID(doctor_token)
    
    request = get_a_request_db(doctor_id, request_id, db)
    updated_request = update_request_status(request, response)
    updated_request_db = update_request_db(updated_request,db)

    request_info = RequestInformation.from_obj(updated_request_db)
    
    return request_info

async def Get_Requests(doctor_token: str, on_status:str, db: Session):
    """Get the all Requests from the DB and then convert into requestinfo model"""
    doctor_id = get_JWT_ID(doctor_token)
    
    requests = get_all_requests_db(doctor_id, db, on_status)
    requests_info = [RequestInformation.from_obj(request) for request in requests]

    return requests_info
    
    
    
