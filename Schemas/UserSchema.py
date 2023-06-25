from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from Schemas.BaseSchema import EntityMeta


class User(EntityMeta):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")
    feelings = relationship('Feeling', back_populates= 'owner')