from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Models.UserModel import UserCreate, UserProfile
from Schemas.BaseSchema import EntityMeta

class User(EntityMeta):
    """Class represent the Schema of User Table in DB"""
    @classmethod
    def from_obj(cls, user: UserCreate, hash_pass: str) -> "User":
        """converter from userCreate object into User object"""
        return cls(
            name=user.name,
            age=user.age,
            email=user.email,
            hashed_password=hash_pass,
            phone=user.phone,
            living_location = user.living_location
            )

    @classmethod
    def from_profile(cls, user: UserProfile) -> "User":
        """converter from userProfile object into User object"""
        return cls(
            name=user.name,
            age=user.age,
            email=user.email,
            diagnose=user.diagnose)

    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    age = Column(Integer)
    phone = Column(String(length=10), index =True)
    living_location = Column(String)
    diagnose = Column(String, default = 'سليم')
    hashed_password = Column(String)
    fcm = Column(String, index= True)
    is_active = Column(Boolean, default=True)
    
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    doctor = relationship('Doctor', back_populates= 'patients')
    feelings = relationship('Feeling', back_populates= 'owner')
    requests = relationship("Request", back_populates="user")
    activities = relationship("Activity", secondary="user_activities", back_populates='users')