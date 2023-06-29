from pydantic import BaseModel
from .FeelingModel import Feeling
class UserBase(BaseModel):
    email: str
    
class UserLogIn(UserBase):
    password: str
    

class UserCreate(UserLogIn): 
    name: str
    age: int 
    confirm_password: str

class User(UserBase):
    id: int
    name: str
    is_active: bool
    feelings: list[Feeling] = []
    fcm: str = None
    doctor_id: int = None
    
    class Config:
        orm_mode = True

class DoctorUser(UserBase):
    name: str
    age: int
    feelings: list[Feeling] = None     
    
class UserUpdate(UserCreate):
    current_password : str = None
    class Config:
        orm_mode = True
        
class UserProfile(UserBase):
    """ Represent values of user's profile """
    name: str
    age: int = None
    
    