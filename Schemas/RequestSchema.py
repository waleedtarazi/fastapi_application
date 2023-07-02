from datetime import datetime
from enum import Enum
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship
from Schemas.BaseSchema import EntityMeta
from enum import Enum as BaseEnum
# from Models.DoctorModel import DoctorProfile


class RequestStatus(str, BaseEnum):
    PINNING = "pinning"
    ACCEPTED = "accepted"
    DENIED = "denied"

class Request(EntityMeta):
    
    # @classmethod
    # def from_obj(cls, request, doctor: DoctorProfile) -> "Request":
    #     """request -> UserAddRequest, return Request"""
    #     print('in the cls of Request schema')
    #     return cls(
    #         doctor = doctor,
    #         user_id = 1
    #     )
    
    __tablename__ = "requests"
    # __table_args__ = (UniqueConstraint('user_id', 'status', name='_user_status_uc'),)

    id = Column(Integer, primary_key=True, index=True)
    status = Column(Enum(RequestStatus), default=RequestStatus.PINNING)
    time_created = Column(DateTime, default=datetime.utcnow)
    
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    doctor = relationship("Doctor", back_populates="requests")
    
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="requests")
    
    