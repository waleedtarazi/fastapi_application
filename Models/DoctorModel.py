from typing import Optional
from pydantic import BaseModel
from Models.UserModel import DoctorUser, UserProfile


class DoctorBase(BaseModel):
    """the base line of Doctor  model"""
    name: Optional[str] = None
    phone: Optional[str] = None
    class Config:
        orm_mode = True
        
class DoctorLogIn(BaseModel):
    """model when Doctor Logs In"""
    email: str
    password: str
    class Config:
        orm_mode = True 

class DoctorCreate(DoctorLogIn, DoctorBase):
    """Represent user model when Create new account"""
    confirm_password: str 
    
class DoctorUpdate(DoctorBase):
    """Represent the user model while Editing his profile"""
    current_password: Optional[str] = None
    new_password: Optional[str] = None
    confirm_new_password: Optional[str] = None

class DoctorProfile(DoctorBase):
    """Represent the user's profile model"""
    email: str
    
    @classmethod
    def from_obj(cls, doctor) -> "DoctorProfile":
        return cls(
            name=doctor.name,
            phone=doctor.phone,
            email=doctor.email,
        )
    

class Doctor(DoctorProfile):
    id: int
    fcm: str = None
    patients: list[UserProfile] = []