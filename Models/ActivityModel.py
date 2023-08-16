from enum import Enum
from pydantic import BaseModel
from Schemas.ActivitySchema import ActivityType


class ActivityBase(BaseModel):
    title: str
    type: ActivityType
    weight: int

class ActivityCreate(ActivityBase):
    pass

class Activity(ActivityBase):
    id: int

    class Config:
        from_attributes = True
