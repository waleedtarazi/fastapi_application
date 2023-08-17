from fastapi import HTTPException
from JWT.jwt_handler import  get_JWT_ID
from Models.FeelingModel import FeelingCreate
from Models.FeelingModel import Feeling as FeelingModel
from Repository.ActivityRepository import update_activity_db
from Repository.FeelingRepository import creat_user_feeling, get_all_feelings, get_feeling_by_date,get_monthly_feelings, update_feeling_db
from Repository.UserRepository import get_user
from sqlalchemy.orm import Session
from Schemas.ActivitySchema import Activity as SchemaActivity
from Schemas.FeelingsSchema import Feeling as SchemaFeelng

async def Get_Feelings(month, year, user_token, db):
    if not user_token:
        raise HTTPException(status_code=401, detail="Not Authorized")
    if not (month and year):
        db_feelings = get_all_feelings(user_id=get_JWT_ID(user_token), db=db)
    else:
        db_feelings = get_monthly_feelings(db=db, id=get_JWT_ID(user_token), year=year, month=month)
    return db_feelings


async def update_feeling_helper(feeling_update:FeelingCreate, old_feeling:SchemaFeelng, db: Session):
    feeling_update_dict = {**vars(feeling_update)}   
    for key, value in feeling_update_dict.items():
        if hasattr(old_feeling, key) and value not in (None, 0, 'None', " ", ""): 
            if getattr(old_feeling, key) != value:
                setattr(old_feeling, key, value)
    updated_feeling = update_feeling_db(old_feeling,db)
    updated_feeling = FeelingModel.from_obj(updated_feeling)
    return updated_feeling

async def Add_Feeling(new_feeling:FeelingCreate, user_token: int, db: Session):
    if not user_token:
        raise HTTPException(status_code=401, detail="Not Authorized")
    user_id = get_JWT_ID(user_token)    
    old_feeling = get_feeling_by_date(user_id=user_id, target_date=new_feeling.created_at, db=db)
    if old_feeling:
        old_feeling = await update_feeling_helper(new_feeling, old_feeling, db)
    else:
        old_feeling = creat_user_feeling(user_id=user_id, feeling=new_feeling, db=db)
    return old_feeling
    

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