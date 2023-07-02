from sqlalchemy.orm import Session
from fastapi import HTTPException
from JWT.jwt_handler import get_JWT_ID
from Repository.RequestRepository import create_request_db
from Repository.auth import get_client_db
from Schemas.UserSchema import User as SchemaUser
from Schemas.DoctorSchema import Doctor as SchemaDoctor
from Schemas.RequestSchema import Request as SchemaRequest
from Models.RequestModel import RequestInformation

def make_request_with_doctor(user_token: str, doctor_id: int, db: Session):
    """ make the doctor request for user"""
    if user_token:
        user_id = get_JWT_ID(user_token)
        request = SchemaRequest(doctor_id=doctor_id, user_id=user_id)
        db_request = create_request_db(request, db)
        user = get_client_db(db, user_id, SchemaUser)
        doctor = get_client_db(db, doctor_id, SchemaDoctor)
        request_info = RequestInformation.from_obj(user,doctor,db_request)
        return request_info
    else:
        raise HTTPException(status_code=402, detail='not authroized')
    
    
def make_request_with_doctor_test(user_id: int, doctor_id: int, db: Session):
    """ """
    request = SchemaRequest(doctor_id=doctor_id, user_id=user_id)
    db_request = create_request_db(request, db)
    
    user = get_client_db(db, user_id, SchemaUser)
    doctor = get_client_db(db, doctor_id, SchemaDoctor)
    request_info = RequestInformation.from_obj(doctor,user, db_request)
    
    
    return request_info
    
    # * old but not gold one 
    # doctor = get_doctor(doctor_id= user_request.doctor_id, db=db)
    # if not doctor:
    #     raise HTTPException(status_code=402, detail="Doctor not found")
    
    # new_request = SchemaRequest(doctor= doctor, user_id= user_request.user_id)
    # doctor.requests.append(new_request)
    # request_db = create_request_db(new_request, db)
    # # request_info = RequestInformation.from_db_request(request_db)
    # return request_db
