from pydantic import BaseModel
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
import datetime
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")
    feelings = relationship('Feeling', back_populates= 'owner')


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="items")
    
class Feeling(Base):
    __tablename__ = 'feelings'
    
    id = Column(Integer, primary_key=True, index=True )
    title = Column(String, index=True)
    confidence = Column(Float, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    message = Column(String, index=True)
    
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', back_populates='feelings')
    