from fastapi import HTTPException
from JWT.jwt_handler import  get_JWT_ID
from Repository.ActivityRepository import update_activity_db
from Repository.FeelingRepository import get_all_feelings, get_monthly_feelings
from Repository.UserRepository import get_user
from sqlalchemy.orm import Session
from Schemas.ActivitySchema import Activity as SchemaActivity

async def Get_Feelings(month, year, user_token, db):
    if not user_token:
        raise HTTPException(status_code=401, detail="Not Authorized")
    if not (month and year):
        db_feelings = get_all_feelings(user_id=get_JWT_ID(user_token), db=db)
    else:
        db_feelings = get_monthly_feelings(db=db, id=get_JWT_ID(user_token), year=year, month=month)
    return db_feelings

async def Get_Activites(token: str, db: Session):
    user_id = get_JWT_ID(token)
    db_user = get_user(user_id= user_id, db=db)
    if db_user:
        db_activities = db_user.activities
        return db_activities
    
async def Update_Activity_Weight(user_token: str, activity_id: int, added_weight: int, db: Session):
    """Update the activity weight"""
    activities = await Get_Activites(user_token, db)
    activity = next((activity for activity in activities if activity.id == activity_id), None)
    activity.weight += added_weight
    updated_activity_db = update_activity_db(activity, db)
    return updated_activity_db