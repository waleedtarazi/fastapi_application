from pydantic import BaseModel
from datetime import datetime
from Schemas.RequestSchema import RequestStatus

class UserAddRequst(BaseModel):
    """The model when user send request to doctor"""
    doctor_id: int
    user_id: int
    description: str
    
class UserRequest(UserAddRequst):
    id: int
    time_created: datetime
    status: RequestStatus
    class Config:
        from_attributes = True
    
class RequestInformation(BaseModel):
    """ Model contain important informations of request"""

    @classmethod
    def from_obj(cls, request) -> "RequestInformation":
        return cls(
            request_id = request.id,
            date = request.time_created,
            user_name = request.user.name,
            doctor_name=request.doctor.name,
            status = request.status,
            description = request.user_description
        )
    request_id: int    
    date: datetime
    user_name: str
    doctor_name: str
    status: str
    description: str
    class Config:
        from_attributes = True
        
    
    
    