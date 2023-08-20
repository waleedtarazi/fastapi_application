import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime,Enum
from sqlalchemy.orm import relationship
from Schemas.BaseSchema import EntityMeta
from enum import Enum as BaseEnum


class FeelingType(str, BaseEnum):
    """Class represent the ENUM of the Request's Status"""
    NEUTRAL = "neutral"
    POSITIVE = "positive"
    NEGATIVE = "negative"

class Feeling(EntityMeta):
    """Class represent the Schema of Feeling Table in DB"""
    
    # @classmethod
    # def from_obj(cls, feeling: FeelingCreate,) -> "Feeling":
    #     """converter into doctor object"""
    #     return cls(
    #         title=feeling.title,
    #         confidence = feeling.confidence)
    
    __tablename__ = 'feelings'
    id = Column(Integer, primary_key=True, index=True )
    type = Column(Enum(FeelingType), default=FeelingType.NEUTRAL,index=True)
    confidence = Column(Float, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    message = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', back_populates='feelings')
