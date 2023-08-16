from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Schemas.BaseSchema import init_db
from Services.Notifications.InitializeNotification import initNotifications
from Metadata.Tags import Tags
from Routes.UserRoute import UserRouter
from Routes.DashboardRoute import DashboardRouter
from Routes.DoctorRoute import DoctorRouter
from Services.Crons.dailyNotification import custom_scheduler


app = FastAPI(
    title="Basita applicatoin \n Release Version",
    version="V 3.0.2",
    openapi_tags=Tags,
)

app.add_middleware(CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'])

app.include_router(UserRouter)
app.include_router(DoctorRouter)
app.include_router(DashboardRouter)


init_db()
initNotifications()
custom_scheduler()

@app.get('/')
async def home_page():
    return{'msg': 'Welcome to our application'}