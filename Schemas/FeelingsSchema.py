import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from Models.FeelingModel import FeelingCreate
from Schemas.BaseSchema import EntityMeta


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
    title = Column(String, index=True)
    confidence = Column(Float, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    message = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', back_populates='feelings')
