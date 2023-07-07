from sqlalchemy.orm import Session
from fastapi import HTTPException
from JWT.jwt_handler import get_JWT_ID
from Repository.RequestRepository import create_request_db
from Schemas.RequestSchema import Request as SchemaRequest
from Models.RequestModel import RequestInformation

def make_request_with_doctor(user_token: str, doctor_id: int, db: Session):
    """ make the doctor request for user"""
    if user_token:
        user_id = get_JWT_ID(user_token)
        request = SchemaRequest(doctor_id=doctor_id, user_id=user_id)
        db_request = create_request_db(request, db)
        request_info = RequestInformation.from_obj(db_request)
        return request_info
    else:
        raise HTTPException(status_code=402, detail='not authroized')