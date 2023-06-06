from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from decouple import config 

db_dialect = config('DB_DIALECT')
db_usr_name = config('DB_USR_NAME')
db_pass = config('DB_PASS')
db_hostname = config('DB_HOSTNAME')
db_name = config('DB_NAME')
db_debug_mode = config('DB_DEBUG_MODE')


# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = f'{db_dialect}://{db_usr_name}:{db_pass}@{db_hostname}/{db_name}'

Engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)

# Base = declarative_base()

def get_db_connection():
    db = scoped_session(SessionLocal)
    try:
        yield db
    finally:
        db.close()