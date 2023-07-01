from fastapi import HTTPException
from JWT.jwt_handler import  get_JWT_ID
from Repository.FeelingRepository import get_all_feelings, get_monthly_feelings

async def Get_Feelings(month, year, user_token, db):
    if not user_token:
        raise HTTPException(status_code=401, detail="Not Authorized")
    if not (month and year):
        db_feelings = get_all_feelings(user_id=get_JWT_ID(user_token), db=db)
    else:
        db_feelings = get_monthly_feelings(db=db, id=get_JWT_ID(user_token), year=year, month=month)
    return db_feelings