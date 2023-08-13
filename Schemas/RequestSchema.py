from datetime import datetime
from enum import Enum as BaseEnum
from sqlalchemy import Column, ForeignKey, Integer, DateTime, Enum, String
from sqlalchemy.orm import relationship
from Schemas.BaseSchema import EntityMeta

class RequestStatus(str, BaseEnum):
    """Class represent the ENUM of the Request's Status"""
    PINNING = "pinning"
    ACCEPTED = "accepted"
    DENIED = "denied"

class Request(EntityMeta):
    """Class represent the Schema of Feeling Table in DB"""
    
    __tablename__ = "requests"
    id = Column(Integer, primary_key=True, index=True)
    status = Column(Enum(RequestStatus), default=RequestStatus.PINNING)
    time_created = Column(DateTime, default=datetime.utcnow)
    user_description = Column(String)
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    doctor = relationship("Doctor", back_populates="requests")
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="requests")
