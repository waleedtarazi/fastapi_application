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
    db_doctor = SchemaDoctor(
        email=doctor.email, hashed_password=hashed_password, name=doctor.name, phone=doctor.phone)
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
    """
    Retrieves requests from the database based on the given doctor ID and requests status.
    
    Args:
        doctor_id (int): The ID of the doctor.
        on_status (str): The status to `filter` requests on.
            if `on_status` is equal to `None` or `all` it will not filter, just all request
        db (Session): The database session.
    
    Returns:
        List of request (SchemaRequest): The specific requests depending on the `status` .
    """

    query = db.query(SchemaRequest)\
        .options(subqueryload(SchemaRequest.user), subqueryload(SchemaRequest.doctor))\
        .filter(SchemaRequest.doctor_id == doctor_id).order_by(SchemaRequest.id)

    if on_status is not None and on_status != 'all':
        query = query.filter(SchemaRequest.status == on_status)

    requests = query.all()

    return requests


def get_a_request_db(doctor_id: int, request_id: int, db: Session):
    """
    Retrieves a specific request from the database based on the given doctor ID and request ID.
    
    Args:
        doctor_id (int): The ID of the doctor.
        request_id (int): The ID of the request.
        db (Session): The database session.
    
    Returns:
        request (SchemaRequest): The specific request object.
    """
    
    request = db.query(SchemaRequest)\
        .filter(SchemaRequest.id == request_id)\
        .filter(SchemaDoctor.id == doctor_id)\
        .first()
    return request
