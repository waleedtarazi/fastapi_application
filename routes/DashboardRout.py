from typing import Union, Optional
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from services.Notifications.UserNotifications import send_notification
from db.database import get_db_connection
from schemas.UserSchema import User
from schemas.FeelingSchema import Feeling
from services.Queries.UserService import get_users, get_user
from services.Queries.FeelingService import get_all_feelings as all_feelings
from services.Queries.FeelingService import calculate_per_month


DashboardRouter = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@DashboardRouter.get("/")
def index():
    raise HTTPException(status_code=404, detail= "no root for this directory for now, please visit us again")


# -------------- Get all useres --------------- 
@DashboardRouter.get("/users", response_model= list[User],tags=['Dashboard'])
async def read_all_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_connection)):
    users = get_users(db, skip=skip, limit=limit)
    return users


# --------------Get all Feelings for all users ----------------
@DashboardRouter.get('/all_feelings', response_model= list[Feeling], tags=['Dashboard']) 
#! not taking in count the none value to get all feelings ->s
async def get_feelings(user_id: Union[int, None] = None, db: Session = Depends(get_db_connection)):
    if user_id:
        if get_user(user_id=user_id, db=db):
            feelings = all_feelings(user_id=user_id, db=db)
            return feelings
        else:
            raise HTTPException(status_code=402, detail="No such user's ID")
    else:
        all_feelings(db=db)


# ---------- Get a specific User ----------------
@DashboardRouter.get("/user", response_model=User, tags=['Dashboard'])
async def read_user(user_id: int, db: Session = Depends(get_db_connection)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# ----------------- mood tracker -----------------------
@DashboardRouter.get('/testing', tags=['Dashboard'])
async def get_mood(user_id: int, db: Session = Depends(get_db_connection)):
    if user_id:
        user_feelings = await get_feelings(user_id=user_id, db=db)
        if user_feelings:
            dig = calculate_per_month(user_feelings)
            return dig
        raise HTTPException(status_code=400, detail="There's no enough data to calculate the Mood")
    raise HTTPException(status_code=402, detail="User not found")


# --------------- send notifications  -------------
class Req(BaseModel):
    title: str
    body: str
       
@DashboardRouter.post("/send-notification", tags=['Dashboard'])
async def send_fcm_notification(request: Req):
    # data = await request.json()
    # token = data.get("token")
    # title = data.get("title")
    # body = data.get("body")
    
    #  Get FCM from user table by ID
    FCM = 'cBpWspdpRY2ywHr8whZMuA:APA91bG1_874mgSkvcxVm8x0KSpzAIXNSc7GSJo3An_pVRBBRdNirKjn3_HD5rWmnqZL1x8PszK2lqj92cQKsbOrVAquFDlujT0EER-9IMAmh0LJ6M60182AwRXTxmTvtv8Wm78wxodw'
    if  not request.title or not request.body:
        raise HTTPException(status_code=400, detail="Missing required parameters")

    send_notification(FCM, request.title, request.body)
    return {"message": "Notification sent"}