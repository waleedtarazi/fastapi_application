from sqlalchemy.orm import Session
from JWT.crypto_handler import get_password_hash
from Schemas.ItemSchema import Item as SchemaItem 
from Schemas.UserSchema import User as SchemaUser
from Models.UserModel import UserCreate, UserUpdate
from Models.ItemModel import ItemCreate


def get_user(db: Session, user_id: int):
    return db.query(SchemaUser).\
        filter(SchemaUser.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(SchemaUser).\
        filter(SchemaUser.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(SchemaUser).\
        offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = SchemaUser(email=user.email, hashed_password=hashed_password, name=user.name )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int ,user_update: UserUpdate):
    user = db.query(SchemaUser).filter(SchemaUser.id == user_id).first()
    user.name = user_update.name
    user.email = user_update.email
    db.commit()
    db.refresh(user)
    return user
    


# ------------- item --------------
def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(SchemaItem).\
        offset(skip).limit(limit).all()

def get_user_items(db: Session, id: int):
    return db.query(SchemaItem).filter(SchemaItem.owner_id == id).all()

def create_user_item(db: Session, item: ItemCreate, user_id: int):
    db_item = SchemaItem(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item




