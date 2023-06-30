import re
from fastapi import HTTPException
from JWT.jwt_handler import signJWT, get_JWT_ID
from JWT.crypto_handler import verify_password
from Repository.DoctorRepository import *
from Repository.UserRepository import get_user_by_email
from Models.UserModel import DoctorUser
from Models.DoctorModel import DoctorProfile

email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

async def Sign_Up(doctor, db):
    if not re.match(email_regex, doctor.email):
        raise HTTPException(status_code=400, detail='Invalid email address')
    if doctor.password != doctor.confirm_password:
        raise HTTPException(status_code=400, detail='Passwords do not match. Please enter matching passwords.')
    db_doctor = get_doctor_by_email(db, doctor.email)
    if db_doctor:
        raise HTTPException(status_code=400, detail='Email already registered.')
    
    created_doctor = create_doctor(db, doctor)
    access_token = signJWT(created_doctor.id)['access_token']
    
    create_doctor = DoctorProfile(name=created_doctor.name, 
                         email=created_doctor.email, 
                         phone=created_doctor.phone)
    
    return {'access_token': access_token, 'doctor': created_doctor}


async def Log_In(doctor, db):
    db_doctor = get_doctor_by_email(db, doctor.email)
    db_user = get_user_by_email(db, doctor.email)
    if (db_doctor is None) or (not db_user is None) or (not verify_password(doctor.password, db_doctor.hashed_password)):
        raise HTTPException(status_code=400, detail='Invalid email or password.')
    
    access_token = signJWT(db_doctor.id)['access_token']
    db_doctor = DoctorProfile(name=db_doctor.name, 
                         email=db_doctor.email, 
                         phone=db_doctor.phone)
    
    return {'access_token': access_token, 'doctor': db_doctor}


async def Get_Profile(doctor_token, db):
    if not doctor_token:
        raise HTTPException(status_code=401, detail='No token provided. Please log in first.')
    doctor_id = get_JWT_ID(doctor_token)
    db_doctor = get_doctor(db, doctor_id)
    if not db_doctor:
        raise HTTPException(status_code=404, detail='Doctor not found.')

    db_doctor = DoctorProfile(name=db_doctor.name, 
                        email=db_doctor.email, 
                        phone=db_doctor.phone)
    return db_doctor


async def Edit_Profile(doctor_update, doctor_token, db):
    if not doctor_token:
        raise HTTPException(status_code=401, detail='Not authorized. Please log in first.')
    doctor_id = get_JWT_ID(doctor_token)
    db_user = get_doctor(db=db, doctor_id=doctor_id)
    
    if not db_user:
        raise HTTPException(status_code=404, detail='Doctor not found.')
    
    user_update_dict = {**vars(doctor_update)}
    for key, value in user_update_dict.items():
        if value is not (None and 0 and 'None') and getattr(db_user, key) != value:
            setattr(db_user, key, value)
    updated_doctor = update_doctor_db(db_user,db)
    
    return DoctorProfile(name=updated_doctor.name, 
                         email=updated_doctor.email, 
                         phone=updated_doctor.phone)


async def Get_Patients(doctor_token, db) -> list[DoctorUser]:
    if not doctor_token:
        raise HTTPException(status_code= 401, detail='Not authorized. Please log in first.')
    doctor_id = get_JWT_ID(doctor_token)
    doctor = get_doctor(db, doctor_id)
    patients = [DoctorUser(name=p.name, age=p.age, email=p.email, feelings=p.feelings) for p in doctor.patients]
    return patients