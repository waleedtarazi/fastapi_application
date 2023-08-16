from fastapi import HTTPException
from JWT.jwt_handler import  get_JWT_ID
from Repository.DoctorRepository import get_doctor
from Models.UserModel import DoctorUser

async def Get_Patients(doctor_token, db) -> list[DoctorUser]:
    if not doctor_token:
        raise HTTPException(status_code= 401, detail='Not authorized. Please log in first.')
    doctor_id = get_JWT_ID(doctor_token)
    doctor = get_doctor(db, doctor_id)
    patients = [DoctorUser(name=p.name, age=p.age, email=p.email, living_location=p.living_location, id=p.id, diagnose=p.diagnose, feelings=p.feelings) for p in doctor.patients]
    return patients