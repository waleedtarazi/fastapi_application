from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Schemas.BaseSchema import initDB
from Services.Notifications.InitializeNotification import initNotifications
from Metadata.Tags import Tags
from Routes.UserRoute import UserRouter
from Routes.DashboardRoute import DashboardRouter
from Services.Crons.dailyNotification import custom_scheduler


app = FastAPI(
    title="MoodBot Stack Development\n pre-release",
    version="V 0.1.1",
    openapi_tags=Tags,
)

app.add_middleware(CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'])

app.include_router(UserRouter)
app.include_router(DashboardRouter)

print('Before init DB')
initDB()
print('After init DB')
initNotifications()
custom_scheduler()

@app.get('/')
async def home_page():
    return{'msg': 'Welcome to our application'}