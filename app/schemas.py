from typing import Union
import datetime

from pydantic import BaseModel, EmailStr

# ------------ item schemas -------------
class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int
    class Config:
        orm_mode = True
        
        
#  ------------------ feeling schemas --------------
class FeelingBase(BaseModel):
    title: str
    
class FeelingCreate(FeelingBase):
    created_at: datetime.datetime
    confidence: float

class Feeling(FeelingCreate):
    id: int
    message: str
    class Config:
        orm_mode = True
    

#  -------------- user base ------------
class UserBase(BaseModel):
    email: EmailStr
    
class UserLogIn(UserBase):
    password: str

class UserCreate(UserLogIn): 
    name: str

class User(UserBase):
    id: int
    name: str
    is_active: bool
    items: list[Item] = []
    feelings: list[Feeling] = []
    class Config:
        orm_mode = True
        
# --------- sentiment --------
# ! the same as feeling, but just matter of not losing the old thing,
# TODO: fix this one :)
class SentimentInput(BaseModel):
    text: str