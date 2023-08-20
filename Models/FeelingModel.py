from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from Schemas.FeelingsSchema import FeelingType

class FeelingBase(BaseModel):
    type: FeelingType
    
class FeelingCreate(FeelingBase):
    confidence: float
    message: Optional[str] = None
    
    class Config:
        from_attributes = True
    # message: str

class Feeling(FeelingCreate):
    
    id: int
    time_created: Optional[datetime] = datetime.utcnow()
    class Config:
        from_attributes = True
    @classmethod
    def from_obj(cls, feeling) -> "Feeling":
        return cls(
            id=feeling.id,
            type=feeling.type,
            message = feeling.message,
            confidence = feeling.confidence,
            created_at = feeling.created_at
        )