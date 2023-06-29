from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Schemas.BaseSchema import EntityMeta

class Doctor(EntityMeta):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    phone = Column(String(length=10), index =True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    fcm = Column(String, index= True)
    
    patients = relationship("User", back_populates="doctor")