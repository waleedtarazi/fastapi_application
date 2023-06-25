from decouple import config 
import firebase_admin
from firebase_admin import credentials

class initNotifications():
    path= config('ADMIN_SDK_PATH')
    cred = credentials.Certificate(path)
    firebase_admin.initialize_app(cred)