from pydantic import BaseModel

from Schemas.RequestSchema import Request
from .UserModel import UserProfile

from datetime import datetime

class UserAddRequst(BaseModel):
    """The model when user send request to doctor"""
    doctor_id: int
    user_id: int
    
class RequestInformation(BaseModel):
    """ Model contain important informations of request"""

    @classmethod
    def from_obj(cls,user, doctor, request) -> "RequestInformation":
        return cls(
           date = request.time_created,
            user_name = user.name,
            doctor_name=doctor.name,
            status = request.status,
        )
        
    date: datetime
    user_name: str
    doctor_name: str
    status: str  
        
    
    
    