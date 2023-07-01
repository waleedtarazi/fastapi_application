from typing import Optional
from pydantic import BaseModel
from .FeelingModel import Feeling
class UserBase(BaseModel):
    """the base line of User model"""
    name: Optional[str] = None
    age: Optional[int] = None
    class Config:
        orm_mode = True
        
class UserLogIn(BaseModel):
    """model when user LogIn"""
    email: str
    password: str
    class Config:
        orm_mode = True 
    
class UserCreate(UserLogIn, UserBase):
    """Represent user model when Create new account"""
    confirm_password: str 


class UserUpdate(UserBase):
    """Represent the user model while Editing his profile"""
    current_password: Optional[str] = None
    new_password: Optional[str] = None
    confirm_new_password: Optional[str] = None
    
        
class UserProfile(UserBase):
    """Represent the user's profile model"""
    email: str
    
    @classmethod
    def from_obj(cls, user) -> "UserProfile":
        return cls(
            name=user.name,
            age=user.age,
            email=user.email,
        )
    
    
class DoctorUser(UserProfile):
    """Represent the user model when Doctor retrive users"""
    feelings: list[Feeling] = []    
    
class User(DoctorUser):
    """Represent the whole user model"""
    id: int
    is_active: bool
    fcm: str = None
    doctor_id: int = None