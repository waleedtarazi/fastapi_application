from typing import Union
import datetime
from pydantic import BaseModel, EmailStr
from .FeelingSchema import Feeling
from .ItemSchema import Item

class UserBase(BaseModel):
    email: EmailStr
    
class UserLogIn(UserBase):
    password: str

class UserCreate(UserLogIn): 
    name: str
    confirm_password: str
    
class UserUpdate(UserBase):
    name: str
    class Config:
        orm_mode = True

class User(UserBase):
    id: int
    name: str
    is_active: bool
    items: list[Item] = []
    feelings: list[Feeling] = []
    class Config:
        orm_mode = True