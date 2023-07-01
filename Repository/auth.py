from typing import Union
from sqlalchemy.orm import Session
from JWT.crypto_handler import get_password_hash
from Models.DoctorModel import DoctorCreate
from Models.UserModel import UserCreate
from Schemas.UserSchema import User as SchemaUser
from Schemas.DoctorSchema import Doctor as SchemaDoctor


def get_client_by_email(db: Session, email: str, client_type: Union[SchemaUser, SchemaDoctor]) -> Union[SchemaDoctor, SchemaUser]:
    return db.query(client_type).\
        filter(client_type.email == email).first()
        
def create_client_db(db: Session, client: Union[UserCreate, DoctorCreate], client_type: Union[SchemaUser, SchemaDoctor]) -> Union[SchemaUser, SchemaDoctor]:
    hashed_password = get_password_hash(client.password)
    db_client = client_type.from_obj(client, hashed_password)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


def get_client_db(db: Session, client_id: int, client_type: Union[SchemaUser, SchemaDoctor]) -> Union[SchemaDoctor, SchemaUser]:
    return db.query(client_type).\
        filter(client_type.id == client_id).first()

def update_client_db(client: Union[SchemaUser, SchemaDoctor], db: Session):
    """Updates the Client information for the specified Client(Doctor/User)."""
    db.commit()
    db.refresh(client)
    return client
