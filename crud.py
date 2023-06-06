# from sqlalchemy import extract, cast, DATE,table, column
# from sqlalchemy.orm import Session
# from app.auth.crypto_handler import get_password_hash
# from ..models import models 
# from ..schemas import schemas
# from datetime import datetime


#  ------------ user ------------
# def get_user(db: Session, user_id: int):
#     return db.query(models.User).\
#         filter(models.User.id == user_id).first()


# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).\
#         filter(models.User.email == email).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).\
#         offset(skip).limit(limit).all()


# def create_user(db: Session, user: schemas.UserCreate):
#     hashed_password = get_password_hash(user.password)
#     db_user = models.User(email=user.email, hashed_password=hashed_password, name=user.name )
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# def update_user(db: Session, user_id: int ,user_update: schemas.UserUpdate):
#     user = db.query(models.User).filter(models.User.id == user_id).first()
#     user.name = user_update.name
#     user.email = user_update.email
#     db.commit()
#     db.refresh(user)
#     return user
    


# # ------------- item --------------
# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).\
#         offset(skip).limit(limit).all()

# def get_user_items(db: Session, id: int):
#     return db.query(models.Item).filter(models.Item.owner_id == id).all()

# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item






# -------------------------- Feeling --------------------------
# def get_all_feelings(db: Session, user_id:int = None):
#     if user_id:
#         print(f'this is the user ID provided is : {user_id}')
#         return db.query(models.Feeling).filter(models.Feeling.owner_id == user_id).all()
#     return db.query(models.Feeling).all()
    

# # -------------------------- Creat Feeling --------------------------
# def creat_user_feeling(db: Session, feeleing: schemas.FeelingCreate, user_id:int):
#     db_item = models.Feeling(**feeleing.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item

# # -------------------------- Get  Mnth Feeling --------------------------
# def get_month(db: Session):
#     print('in monthhh')
#     year_q = extract('year', models.Feeling.created_at)
#     return db.query(models.Feeling).filter(year_q == 2023,models.Feeling.owner_id == 1).all()

# -------------------------- Get  Mnth Feeling --------------------------
# def get_monthly_feelings(db: Session, id:int, year:int = 0, month:int = 0):
#     start_date = datetime(year=year, month=month,day=1)
#     end_date = datetime(year=year, month=month+1, day=1)
#     return db.query(models.Feeling).filter(models.Feeling.created_at > start_date, models.Feeling.created_at < end_date).all()
    
    # ! the below works but it's super costy
    # filtered_feelings = []
    # filtered_feelings = db.query(models.Feeling).filter(models.Feeling.created_at.in_([start_date,end_date])).all()
    # for feeling in feelings:
    #     print(type(feeling))
    #     if feeling.created_at.month == month and feeling.created_at.year == year:
    #         filtered_feelings.append(feeling)
    # ! the above works but it's super costy
 
 
 # -------------------------- Seeding Feeling --------------------------           
# def seeding(db: Session, user_id:int):
#     seed_feelings = [
#         {"title": "negative", "confidence": 0.2, 'message':'message one', 'owner_id':1},
#         {"title": "positive", "confidence": .4, 'message':'message two', 'owner_id':1},
#         {"title": "negative", "confidence":1.4, 'message':'message three', 'owner_id':1},
#         {"title": "negative", "confidence":1.4, 'message':'message three', 'owner_id':1},
#     ]
#     for feeling in seed_feelings:
#         feeling = models.Feeling(**feeling)
#         db.add(feeling)
#         db.commit()
#         db.refresh(feeling)
               
        
# def calculate_per_month(feelings: list[schemas.Feeling]):
#     sad_ratio = 0
#     sad_ratio = sum(1 for feeling in feelings if feeling.title == 'sad')
#     if sad_ratio >= len(feelings) * .8:
#         return {'user_status':'probably have some real disorder like depression'}
#     elif sad_ratio >= len(feelings) *.5:
#         return {'user_status': 'may have personality disorder'}
#     else:
#         return{'user_status':'having nothing serious take care of yourself dear customer'}


# highest_float = -float('inf')  # Starting value for highest float
# for feeling in feelings:
#     if isinstance(feeling.height, float) and feeling.height > highest_float:
#         highest_float = feeling.height
    
    