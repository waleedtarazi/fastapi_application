from sqlalchemy.orm import Session
from auth.crypto_handler import get_password_hash
from models.ItemModel import Item as mItem 
from models.UserModel import User as mUser
from schemas.UserSchema import UserCreate, UserUpdate
from schemas.ItemSchema import ItemCreate


def get_user(db: Session, user_id: int):
    return db.query(mUser).\
        filter(mUser.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(mUser).\
        filter(mUser.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(mUser).\
        offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = mUser(email=user.email, hashed_password=hashed_password, name=user.name )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int ,user_update: UserUpdate):
    user = db.query(mUser).filter(mUser.id == user_id).first()
    user.name = user_update.name
    user.email = user_update.email
    db.commit()
    db.refresh(user)
    return user
    


# ------------- item --------------
def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(mItem).\
        offset(skip).limit(limit).all()

def get_user_items(db: Session, id: int):
    return db.query(mItem).filter(mItem.owner_id == id).all()

def create_user_item(db: Session, item: ItemCreate, user_id: int):
    db_item = mItem(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item




