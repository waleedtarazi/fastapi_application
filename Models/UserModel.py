from pydantic import BaseModel
from .FeelingModel import Feeling

class UserBase(BaseModel):
    email: str
    
class UserLogIn(UserBase):
    password: str
    
    class Config:
        schema_extra = {
            'example': {
                'email': 'programmer@python.com',
                'password' : 'IDK my password'
            }
        }

class UserCreate(UserLogIn): 
    name: str
    confirm_password: str

    class Config:
        schema_extra = {
            "example": {
                "name": "programmer",
                "email": "programmer@python.com",
                "password": "python",
                "confirm_password": "python"
            }
        }
    
class UserUpdate(UserBase):
    name: str
    class Config:
        orm_mode = True

class User(UserBase):
    id: int
    name: str
    is_active: bool
    feelings: list[Feeling] = []
    class Config:
        orm_mode = True