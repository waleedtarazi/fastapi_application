from typing import Union
from pydantic import BaseModel
from Models.UserModel import UserBase

# ------------ Doctor schemas -------------
class DoctorBase(BaseModel):
    email: str

class DoctorLogIn(DoctorBase):
    password: str

class DoctorCreate(DoctorLogIn):
    email: str
    confirm_password: str
    name: str
    phone: str = "None"
    class Config:
        orm_mode = True
    
class Doctor(DoctorCreate):
    id: int
    fcm: str = "None"
    patients: list[UserBase] = []
    class Config:
        orm_mode = True
        
class DoctorUpdate(DoctorCreate):
    current_password: str
    pass
    