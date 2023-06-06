from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship
from models.BaseModel import EntityMeta

class Item(EntityMeta):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="items")