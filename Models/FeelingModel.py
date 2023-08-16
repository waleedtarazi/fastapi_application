import datetime
from pydantic import BaseModel


class FeelingBase(BaseModel):
    title: str
    
class FeelingCreate(FeelingBase):
    created_at: datetime.datetime
    confidence: float

class Feeling(FeelingCreate):
    id: int
    message: str
    class Config:
        from_attributes = True