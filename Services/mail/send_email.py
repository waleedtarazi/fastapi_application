from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from decouple import config
from Models.EmailModel import Email
from pathlib import Path


MAIL_USERNAME = config('MAIL_USERNAME')
MAIL_PASSWORD = config('MAIL_PASSWORD')
MAIL_FROM = config('MAIL_FROM')
MAIL_PORT = config('MAIL_PORT')
MAIL_SERVER = config('MAIL_SERVER')
MAIL_FROM_NAME = config('MAIL_FROM_NAME')


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

 
async def simple_send(email: Email):
    html = """<p>Hi this test mail, thanks for using Fastapi-mail</p> """

    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=email.dict().get("email"),
        body=html,
        subtype=MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)

async def send_email(informations: Email):
    message = MessageSchema(
        subject='Welcome to Basita application',
        recipients=[informations.email],
        template_body={'user_name': informations.user_name},
        subtype=MessageType.html
    )
    fm = FastMail(conf)
    await fm.send_message(message, template_name='warrning.html',)
    
    