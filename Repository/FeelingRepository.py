from sqlalchemy.orm import Session
from sqlalchemy.sql import cast
from sqlalchemy import extract
from Schemas.FeelingsSchema import Feeling as SchemaFeeling
from Models.FeelingModel import FeelingCreate, Feeling
from datetime import datetime


def get_all_feelings(db: Session, user_id:int = None):
    if user_id:
        return db.query(SchemaFeeling).filter(SchemaFeeling.owner_id == user_id).all()
    return db.query(SchemaFeeling).all()
    

# -------------------------- Creat Feeling --------------------------
def creat_user_feeling(db: Session, feeling: FeelingCreate, user_id:int):
    print("in feeling Repo", feeling)
    db_item = SchemaFeeling(**feeling.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_feeling_by_date(user_id: int, target_date: datetime.date, db: Session):
    print(target_date)
    day = target_date.day
    month = target_date.month
    year = target_date.year
    start_date = datetime(year=year, month=month,day=day)
    end_date = datetime(year=year, month=month, day=day+1)
    feelings = db.query(SchemaFeeling).filter(
        SchemaFeeling.owner_id == user_id,
        SchemaFeeling.created_at>= start_date, SchemaFeeling.created_at < end_date).first()
    return feelings

def update_feeling_db(feeling: SchemaFeeling, db: Session):
    """ update the current request into DB """
    db.commit()
    db.refresh(feeling)
    return feeling

def get_monthly_feelings(db: Session, id:int, 
                         year:int = 0, 
                         month:int = 0):
    start_date = datetime(year=year, month=month,day=1)
    end_date = datetime(year=year, month=month+1, day=1)
    return db.query(SchemaFeeling).filter(SchemaFeeling.created_at > start_date, SchemaFeeling.created_at < end_date).all()


# def seeding(db: Session, user_id:int):
#     seed_feelings = [
#         {"title": "negative", "confidence": 0.2, 'message':'message one', 'owner_id':1},
#         {"title": "positive", "confidence": .4, 'message':'message two', 'owner_id':1},
#         {"title": "negative", "confidence":1.4, 'message':'message three', 'owner_id':1},
#         {"title": "negative", "confidence":1.4, 'message':'message three', 'owner_id':1},
#     ]
#     for feeling in seed_feelings:
#         feeling = mFeeling(**feeling)
#         db.add(feeling)
#         db.commit()
#         db.refresh(feeling)
               
        
def calculate_per_month(feelings: list[Feeling]):
    sad_ratio = 0
    sad_ratio = sum(1 for feeling in feelings if feeling.title == 'negative')
    if sad_ratio >= len(feelings) * .8:
        return {'user_status':'probably have some real disorder like depression'}
    elif sad_ratio >= len(feelings) *.5:
        return {'user_status': 'may have personality disorder'}
    else:
        return{'user_status':'having nothing serious take care of yourself dear customer'}