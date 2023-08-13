from fastapi import Depends
from sqlalchemy.orm import Session,joinedload, subqueryload
from Schemas.ActivitySchema import Activity as SchemaActivity
from Models.ActivityModel import ActivityCreate
from .UserRepository import get_users


def get_activities(db: Session):
    activities = db.query(SchemaActivity).all()
    return activities

def add_activity(activity: SchemaActivity, db: Session):
    """Make new activity"""
    db.add(activity)
    add_activity_to_all_users(db=db, activity= activity)
    db.commit()
    return activity

def add_activity_to_all_users(db: Session, activity: SchemaActivity):
    """Add the activity to all users"""
    users = get_users(db=db)
    for user in users:
        user.activities.append(activity)
        
def update_activity_db(activity: SchemaActivity, db: Session):
    """ update the current activity into DB """
    db.commit()
    db.refresh(activity)
    return activity
