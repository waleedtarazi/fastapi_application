from apscheduler.schedulers.background import BackgroundScheduler
import datetime
from Services.Notifications.SendNotifications import send_notification


FCM = 'cBpWspdpRY2ywHr8whZMuA:APA91bG1_874mgSkvcxVm8x0KSpzAIXNSc7GSJo3An_pVRBBRdNirKjn3_HD5rWmnqZL1x8PszK2lqj92cQKsbOrVAquFDlujT0EER-9IMAmh0LJ6M60182AwRXTxmTvtv8Wm78wxodw'


def daily_job():
    send_notification(token= FCM, title='cron job from server', body=f'test body{datetime.datetime.now()}')
    print("Daily job running at", datetime.datetime.now())

def custom_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(daily_job, 'cron', hour=9, minute=30)
    scheduler.start()