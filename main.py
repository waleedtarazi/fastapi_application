from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.BaseModel import init
from metadata.Tags import Tags
from routes.UserRoute import UserRouter
from routes.DashboardRout import DashboardRouter


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

init()