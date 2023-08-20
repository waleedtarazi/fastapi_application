from typing import Union
from sqlalchemy.orm import Session
from Models.ActivityModel import ActivityCreate
from Models.EmailModel import Email
from Models.NotificationModel import Notificatoin
from Services.mail.send_email import send_email, send_warrning_email
from db.database import get_db_connection
from Models.FeelingModel import Feeling
from fastapi import (APIRouter, 
                     Depends, 
                     HTTPException)
from Services.DashboardService.dashboardService import (
    Read_All_Doctors,
    Read_All_Users, 
    Get_Feelings,
    Read_Doctor, 
    Read_User, 
    Get_Mood,
    Send_FCM_Notification,
    add_users_activity,
    get_all_activities) 

DashboardRouter = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@DashboardRouter.get("/")
def index():
    raise HTTPException(status_code=404, detail= "no root for this directory for now, please visit us again")


#* Get all useres 
@DashboardRouter.get("/users", tags=['Dashboard'])
async def read_all_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_connection)):
    return await Read_All_Users(skip, limit, db)

#* Get all doctors
@DashboardRouter.get('/doctors',  tags=['Dashboard'])
async def read_all_doctors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_connection)):
    return await Read_All_Doctors(skip, limit, db)

#* Get all Feelings for all users 
@DashboardRouter.get('/all_feelings', response_model= list[Feeling], tags=['Dashboard']) 
async def get_feelings(user_id: Union[int, None] = None, db: Session = Depends(get_db_connection)):
    return await Get_Feelings(user_id, db)


#* Get a specific User 
@DashboardRouter.get("/user", tags=['Dashboard'])
async def get_user(user_id: int, db: Session = Depends(get_db_connection)):
    return await Read_User(user_id, db)

#* Get a specific Doctor 
@DashboardRouter.get("/doctor", tags=['Dashboard'])
async def get_doctor(doctor_id: int, db: Session = Depends(get_db_connection)):
    return await Read_Doctor(doctor_id, db)

#* mood tracker
@DashboardRouter.get('/testing', tags=['Dashboard'])
async def get_mood(user_id: int, db: Session = Depends(get_db_connection)):
    return await Get_Mood(user_id, db)

#* send notification   
@DashboardRouter.post("/send-notification", tags=['Dashboard'])
async def send_fcm_notification(notification: Notificatoin):
    return await Send_FCM_Notification(notification)

#* get all activities
@DashboardRouter.get('/activities', tags=['Dashboard'])
async def all_activities(db: Session = Depends(get_db_connection)):
    return await get_all_activities(db)

#* add an activity to all users
@DashboardRouter.post("/activities/add", tags=['Dashboard'])
async def add_activity_all_users(activity: ActivityCreate, db: Session = Depends(get_db_connection)):
    return await add_users_activity(activity=activity, db=db)

#* send Email
@DashboardRouter.post('/send-email')
async def send_email_to_admin(user_token: str, message:str, db: Session = Depends(get_db_connection)):
    await send_warrning_email(user_token, message, db)
    return {'status': '200', 'message':'Email sent successfully'}


@DashboardRouter.post('/fake-message')
async def send_fake_message(message: str, buttons: bool):
    if buttons:
       data = [{'recipient_id': 'default',
             'text': 'السلام عليكم ,كيف حالك؟',
             'buttons': [
                 {'title': 'هل تريد مساعدة؟', 'payload': '/help'},
                 {'title': 'هل تريد الفضفضة؟', 'payload': '/feelings_express'}]}]  
    else:
        data = [{'recipient_id': 'default',
                 'text': 'السلام عليكم ,كيف حالك؟'}]
    return data