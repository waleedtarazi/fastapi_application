from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from decouple import config
from JWT.jwt_handler import get_JWT_ID
from Models.EmailModel import Email
from pathlib import Path

from Repository.UserRepository import get_user


MAIL_USERNAME = config('MAIL_USERNAME')
MAIL_PASSWORD = config('MAIL_PASSWORD')
MAIL_FROM = config('MAIL_FROM')
MAIL_PORT = config('MAIL_PORT')
MAIL_SERVER = config('MAIL_SERVER')
MAIL_FROM_NAME = config('MAIL_FROM_NAME')
ADMIN_MAIL = config('ADMIN_MAIL')


conf = ConnectionConfig(
    MAIL_USERNAME= MAIL_USERNAME,
    MAIL_PASSWORD= MAIL_PASSWORD,
    MAIL_FROM= MAIL_FROM,
    MAIL_PORT= MAIL_PORT,
    MAIL_SERVER= MAIL_SERVER,
    MAIL_FROM_NAME=MAIL_FROM_NAME ,
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True,
    TEMPLATE_FOLDER= Path('Services/mail/Templates/'),
)

async def send_warrning_email(user_token: str, message:str, db):
    user_id = 1
    # get_JWT_ID(user_token)
    user_name = get_user(db, user_id).name
    _Email = Email(email=ADMIN_MAIL,user_name=user_name, message=message)
    return await send_email(_Email)

async def send_email(informations: Email):
    message = MessageSchema(
        subject='Welcome to Basita application',
        recipients=[informations.email],
        template_body={'user_name': informations.user_name,
                       'user_message': informations.message},
        subtype=MessageType.html
    )
    fm = FastMail(conf)
    await fm.send_message(message, template_name='warrning.html',)
    
    