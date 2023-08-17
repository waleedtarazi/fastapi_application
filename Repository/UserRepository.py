from sqlalchemy.orm import Session, subqueryload
from JWT.crypto_handler import get_password_hash
from Schemas.UserSchema import User as SchemaUser
from Models.UserModel import UserCreate
from Schemas.RequestSchema import Request as SchemaRequest



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

def update_user_db(user, db: Session):
    """Updates the user information for the specified user."""
    db.commit()
    db.refresh(user)
    return user


def get_my_requests_db(user_id: int, db: Session):

    query = db.query(SchemaRequest)\
        .options(subqueryload(SchemaRequest.user), subqueryload(SchemaRequest.doctor))\
        .filter(SchemaRequest.user_id == user_id).order_by(SchemaRequest.id)

    # if on_status is not None and on_status != 'all':
    #     query = query.filter(SchemaRequest.status == on_status)

    requests = query.all()

    return requests