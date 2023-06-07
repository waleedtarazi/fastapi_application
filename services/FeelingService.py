from sqlalchemy.orm import Session
from models.FeelingsModel import Feeling as mFeeling
from schemas.FeelingSchema import FeelingCreate, Feeling
from datetime import datetime


def get_all_feelings(db: Session, user_id:int = None):
    if user_id:
        return db.query(mFeeling).filter(mFeeling.owner_id == user_id).all()
    return db.query(mFeeling).all()
    

# -------------------------- Creat Feeling --------------------------
def creat_user_feeling(db: Session, feeleing: FeelingCreate, user_id:int):
    db_item = mFeeling(**feeleing.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_monthly_feelings(db: Session, id:int, year:int = 0, month:int = 0):
    start_date = datetime(year=year, month=month,day=1)
    end_date = datetime(year=year, month=month+1, day=1)
    return db.query(mFeeling).filter(mFeeling.created_at > start_date, mFeeling.created_at < end_date).all()


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