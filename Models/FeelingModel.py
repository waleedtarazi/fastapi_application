import datetime
from typing import Optional
from pydantic import BaseModel


class FeelingBase(BaseModel):
    title: str
    
class FeelingCreate(FeelingBase):
    created_at: datetime.datetime
    confidence: float
    message: Optional[str] = None
    
    class Config:
        from_attributes = True
    # message: str

class Feeling(FeelingCreate):
    
    id: int
    class Config:
        from_attributes = True
    @classmethod
    def from_obj(cls, feeling) -> "Feeling":
        return cls(
            title=feeling.title,
            id = feeling.id,
            message = feeling.message,
            confidence = feeling.confidence,
            created_at = feeling.created_at
        )