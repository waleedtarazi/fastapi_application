from sqlalchemy.orm import Session
from sql_app.auth.crypto_handler import get_password_hash 
from . import models, schemas
import datetime

#  ------------ user ------------
def get_user(db: Session, user_id: int):
    return db.query(models.User).\
        filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).\
        filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).\
        offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password, name=user.name )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# ------------- item --------------
def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).\
        offset(skip).limit(limit).all()

def get_user_items(db: Session, id: int):
    return db.query(models.Item).filter(models.Item.owner_id == id).all()

def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# ------------- feeling -------
def get_all_feelings(db: Session, skip: int = 0, limit: int = 30):
    return db.query(models.Feeling).offset(skip).limit(limit).all()

def creat_user_feeling(db: Session, feeleing: schemas.FeelingCreate, user_id:int):
    db_item = models.Feeling(**feeleing.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_user_feelings(db: Session, id:int, year:int, month:int):
    return db.\
        query(models.Feeling).\
        filter(models.Feeling.created_at.year == year,
               models.Feeling.created_at.month == month,
               models.Feeling.owner_id == id).\
            all()
            
def seeding(db: Session, user_id:int):
    seed_feelings = [
        {"title": "anger", "confidence": 0.2, 'message':'message one'},
        {"title": "sad", "confidence": .4, 'message':'message two'},
        {"title": "fun", "confidence":1.4, 'message':'message three'},
    ]
    for feeling in seed_feelings:
        feeling = models.Feeling(**feeling)
        db.add(feeling)
        db.commit()
        db.refresh(feeling)