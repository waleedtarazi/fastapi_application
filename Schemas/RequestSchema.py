from datetime import datetime
from enum import Enum
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship
from Schemas.BaseSchema import EntityMeta
from enum import Enum as BaseEnum


class RequestStatus(str, BaseEnum):
    PINNING = "pinning"
    ACCEPTED = "accepted"
    DENIED = "denied"

class Request(EntityMeta):
    
    __tablename__ = "requests"
    # __table_args__ = (UniqueConstraint('user_id', 'status', name='_user_status_uc'),)

    id = Column(Integer, primary_key=True, index=True)
    status = Column(Enum(RequestStatus), default=RequestStatus.PINNING)
    time_created = Column(DateTime, default=datetime.utcnow)
    # user_description = Column(String)
    # doctor_description = Column(String)
    
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    doctor = relationship("Doctor", back_populates="requests")
    
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="requests")
    

#  # Add the new column to the existing table]
# def add_new_column():
#     from sqlalchemy import create_engine
#     from sqlalchemy.orm import sessionmaker
#     engine = create_engine('your_database_connection_string')
#     Session = sessionmaker(bind=engine)
#     session = Session()
#      # Reflect the changes made to the database schema
#     EntityMeta.metadata.reflect(engine)
#      # Add the new column to the table
#     if not hasattr(Request, 'user_description'):
#         user_description = Column('user_description', String)
#         user_description.create(Request.__table__)
#         session.commit()
#     session.close()

# # Call the function to add the new column
# add_new_column()
    