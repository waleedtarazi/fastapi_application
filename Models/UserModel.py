from typing import Optional
from pydantic import BaseModel

from Models.RequestModel import RequestInformation, UserRequest
from .FeelingModel import Feeling
class UserBase(BaseModel):
    """the base line of User model"""
    name: Optional[str] = None
    age: Optional[int] = None
    phone: Optional[str] = None
    living_location : Optional[str] = None
    class Config:
        from_attributes = True
        
class UserLogIn(BaseModel):
    """model when user LogIn"""
    email: str
    password: str
    class Config:
        from_attributes = True 
    
class UserCreate(UserLogIn, UserBase):
    """Represent user model when Create new account"""
    confirm_password: str 


class UserUpdate(UserBase):
    """Represent the user model while Editing his profile"""
    current_password: Optional[str] = None
    new_password: Optional[str] = None
    confirm_new_password: Optional[str] = None
    diagnose: Optional[str] = None
    
        
class UserProfile(UserBase):
    """Represent the user's profile model"""
    email: str
    id: int
    diagnose: str
    
    @classmethod
    def from_obj(cls, user) -> "UserProfile":
        return cls(
            name=user.name,
            age=user.age,
            email=user.email,
            living_location = user.living_location,
            phone = user.phone,
            id = user.id,
            diagnose = user.diagnose
        )
    
    
class DoctorUser(UserProfile):
    """Represent the user model when Doctor retrive users"""
    feelings: list[Feeling] = []
    diagnose: str
    
class User(DoctorUser):
    """Represent the whole user model"""
    id: int
    fcm: str = None
    doctor_id: int = None
    requests: list[UserRequest]
    is_active: bool