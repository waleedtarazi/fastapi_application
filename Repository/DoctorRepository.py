from sqlalchemy.orm import Session, subqueryload
from JWT.crypto_handler import get_password_hash
from Schemas.DoctorSchema import Doctor as SchemaDoctor
from Schemas.UserSchema import User as SchemaUser
from Schemas.RequestSchema import Request as SchemaRequest
from Models.DoctorModel import DoctorCreate


def get_doctor(db: Session, doctor_id: int):
    return db.query(SchemaDoctor).\
        filter(SchemaDoctor.id == doctor_id).first()


def get_doctor_by_email(db: Session, email: str):
    return db.query(SchemaDoctor).\
        filter(SchemaDoctor.email == email).first()


def get_doctors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(SchemaDoctor).\
        offset(skip).limit(limit).all()


def create_doctor(db: Session, doctor: DoctorCreate):
    hashed_password = get_password_hash(doctor.password)
    db_doctor = SchemaDoctor(email=doctor.email, hashed_password=hashed_password, name=doctor.name, phone=doctor.phone )
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

def update_doctor_db(doctor, db: Session):
    """Updates the Doctor information for the specified user."""
    db.commit()
    db.refresh(doctor)
    return doctor


def get_all_requests_db(doctor_id: int, db: Session, on_status: str):
    """ get all Requests for the doctor """
    requests = db.query(SchemaRequest)\
    .options(subqueryload(SchemaRequest.user), subqueryload(SchemaRequest.doctor))\
    .filter(SchemaRequest.doctor_id == doctor_id)\
    .filter(SchemaRequest.status == on_status)\
    .all()
    
    # requests = db.query(SchemaRequest)\
    #     .filter(SchemaDoctor.id == doctor_id)\
    #     .all()
    
    return requests


def get_a_request_db(doctor_id: int, request_id:int, db: Session):
    """ get a specific Request """
    request = db.query(SchemaRequest)\
        .filter(SchemaRequest.id == request_id)\
        .filter(SchemaDoctor.id == doctor_id)\
        .first()
        # the prvious but not working
        # .join(SchemaUser)\
        # .join(SchemaDoctor)\
        # .filter(SchemaRequest.id == request_id)\
        # .filter(SchemaDoctor.id == 1)\
        # .first()
        
        # i dont know the below
        # .filter(Request.doctor_id == doctor_id)\
        # .filter(Request.user_id == user_id)\
        # .filter(Request.status == 'open')\
        # .all()   
        
    return request




