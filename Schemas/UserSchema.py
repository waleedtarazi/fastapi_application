from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Schemas.BaseSchema import EntityMeta
from Schemas.DoctorSchema import Doctor


class User(EntityMeta):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    hashed_password = Column(String)
    age = Column(Integer)
    phone = Column(String(length=10), index =True)
    fcm = Column(String, index= True)
    is_active = Column(Boolean, default=True)

    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    doctor = relationship('Doctor', back_populates= 'patients')
    
    feelings = relationship('Feeling', back_populates= 'owner')