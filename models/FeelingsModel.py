from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
import datetime
from models.BaseModel import EntityMeta


class Feeling(EntityMeta):
    __tablename__ = 'feelings'
    
    id = Column(Integer, primary_key=True, index=True )
    title = Column(String, index=True)
    confidence = Column(Float, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    message = Column(String, index=True)
    
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', back_populates='feelings')