from typing import Union
from fastapi import Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from Services.UserService.userService import Get_Feelings
from Services.Notifications.SendNotifications import send_notification
from db.database import get_db_connection
from Repository.UserRepository import get_users, get_user
from Repository.FeelingRepository import get_all_feelings as all_feelings
from Repository.FeelingRepository import calculate_per_month
from Models.NotificationModel import Notificatoin


async def Read_All_Users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_connection)):
    users = get_users(db, skip=skip, limit=limit)
    return users


#! not taking in count the none value to get all feelings ->s
async def Get_Feelings(user_id: Union[int, None] = None, db: Session = Depends(get_db_connection)):
    if user_id:
        if get_user(user_id=user_id, db=db):
            feelings = all_feelings(user_id=user_id, db=db)
            return feelings
        else:
            raise HTTPException(status_code=402, detail="No such user's ID")
    else:
        all_feelings(db=db)
        
async def Read_User(user_id: int, db: Session = Depends(get_db_connection)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user



async def Get_Mood(user_id: int, db: Session = Depends(get_db_connection)):
    if user_id:
        user_feelings = await Get_Feelings(user_id=user_id, db=db)
        if user_feelings:
            dig = calculate_per_month(user_feelings)
            return dig
        raise HTTPException(status_code=400, detail="There's no enough data to calculate the Mood")
    raise HTTPException(status_code=402, detail="User not found")



# Send notifications 
class Req(BaseModel):
    title: str
    body: str
async def Send_FCM_Notification(notification: Notificatoin):
    #!  Get FCM from user table by ID
    if  not notification.title or not notification.body:
        raise HTTPException(status_code=400, detail="Missing required parameters")

    send_notification(notification.fcm, notification.title, notification.body)
    return {"message": "Notification sent"}