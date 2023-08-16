from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Models.DoctorModel import DoctorCreate
from Schemas.BaseSchema import EntityMeta

class Doctor(EntityMeta):
    """Class represent the Schema of Doctor Table in DB""" 
    @classmethod
    def from_obj(cls, doctor: DoctorCreate, hash_password: str) -> "Doctor":
        """converter into doctor object"""
        return cls(
            name=doctor.name,
            phone=doctor.phone,
            email=doctor.email,
            hashed_password=hash_password,
            clinic_location = doctor.clinic_location)
    __tablename__ = "doctors"
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    phone = Column(String(length=10), index =True)
    clinic_location = Column(String)
    fcm = Column(String, index= True)
    patients = relationship("User", back_populates="doctor")
    requests = relationship("Request", back_populates="doctor")
