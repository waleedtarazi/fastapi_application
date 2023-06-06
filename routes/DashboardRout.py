from typing import Union, Optional
from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from auth.jwt_handler import signJWT, get_JWT_ID
from auth.crypto_handler import verify_password
from db.database import get_db_connection
from schemas.UserSchema import User
from schemas.FeelingSchema import Feeling
from services.UserService import get_users, get_user
from services.FeelingService import get_all_feelings as all_feelings


DashboardRouter = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@DashboardRouter.get("/")
def index():
    raise HTTPException(status_code=404, detail= "no root for this directory for now, please visit us again")

# -------------- Get all useres --------------- 
@DashboardRouter.get("/users", response_model= list[User],tags=['Dashboard'])
async def read_all_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_connection)):
    users = get_users(db, skip=skip, limit=limit)
    print(users[0])
    return users

# ---------- Get specific User ----------------
@DashboardRouter.get("/{user_id}", response_model=User, tags=['Dashboard'])
async def read_user(user_id: int, db: Session = Depends(get_db_connection)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# --------------Get all Feelings for all users ----------------
# @DashboardRouter.get('/all', tags=['Dashboard'])
# def _():
#     return {}
    