from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Table
from sqlalchemy.orm import relationship
from Schemas.BaseSchema import EntityMeta
from enum import Enum as BaseEnum

class ActivityType(str, BaseEnum):
    """Class represent the ENUM of the Activity's Type"""
    POSITIVE = "positive"
    NEGATIVE = "negative"
    NUTRAL = "nutral"


user_activities = Table('user_activities', EntityMeta.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('activity_id', ForeignKey('activities.id'), primary_key=True)
)

class Activity(EntityMeta):
    __tablename__ = 'activities'
    
    id = Column(Integer, primary_key=True, index= True)
    title = Column(String, nullable=False )
    type = Column(Enum(ActivityType), nullable=False, default=ActivityType.NUTRAL)
    weight = Column(Integer,default=0)
    users = relationship("User", secondary="user_activities", back_populates='activities')
    


