from typing import List
from pydantic import BaseModel, EmailStr


class Email(BaseModel):
    email: EmailStr
    user_name: str
    message: str