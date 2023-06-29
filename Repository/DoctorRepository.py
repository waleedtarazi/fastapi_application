from sqlalchemy.orm import Session
from JWT.crypto_handler import get_password_hash
from Schemas.DoctorSchema import Doctor as SchemaDoctor
from Models.DoctorModel import DoctorCreate, DoctorUpdate


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
    db_doctor = SchemaDoctor(email=doctor.email, hashed_password=hashed_password, name=doctor.name )
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

def update_doctor(db: Session, doctor_id: int ,doctor_update: DoctorUpdate):
    doctor = db.query(SchemaDoctor).filter(SchemaDoctor.id == doctor_id).first()
    doctor.name = doctor_update.name
    doctor.email = doctor_update.email
    db.commit()
    db.refresh(doctor)
    return doctor
    




