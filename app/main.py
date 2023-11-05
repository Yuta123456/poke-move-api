from dotenv import load_dotenv

load_dotenv()
from fastapi.security import OAuth2PasswordBearer

from app.database.crud import get_challenge_by_id, get_type, get_user_by_id
from app.database.models import Quiz, User
from app.service.auth import create_user, verify_access_token
from app.service.challenge import create_challenge


import sys
import os

sys.path.append("app")
from enum import Enum
from fastapi import Depends, FastAPI, HTTPException

# from database.crud import create_user

from app.database.main import Base, SessionLocal, engine
from sqlalchemy.orm import Session

from app.database.schemas import UserCreate

# モデルにある全部をcreate tableしてくれる
Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Level(Enum):
    LOW = "low"
    MIDDLE = "middle"
    HIGH = "high"

    def contains(self, value):
        return value in [i.value for i in self]


@app.get("/")
def root():
    return {"message": "hello world"}


# http://localhost:8000/quiz?level=high
@app.get("/quiz")
async def root(level: str, db: Session = Depends(get_db)):
    if level == Level.HIGH.value:
        return {level: "high"}
    elif level == Level.MIDDLE.value:
        return {level: "middle"}
    elif level == Level.LOW.value:
        return {level: "low"}
    else:
        raise HTTPException(
            status_code=400,
            detail="Make sure you specified the level correctly in query parameter.",
        )


@app.get("/user")
def user(db: Session = Depends(get_db)):
    user = create_user(db)
    print(user.api_token, user.id, user.refresh_token)
    return user


@app.get("/challenge")
async def challenge(
    db: Session = Depends(get_db), user_id: dict = Depends(verify_access_token)
):
    user = get_user_by_id(db, user_id)
    challenge = create_challenge(db, user)
    res = {
        "challenge_id": challenge.id,
    }
    return res


@app.get("/type/{id}")
async def type(id: int, db: Session = Depends(get_db)):
    type = get_type(db, id)
    return type


@app.get("/challenge/{challenge_id}/quiz")
async def get_quiz(challenge_id: int, db: Session = Depends(get_db)):
    challenge = get_challenge_by_id(db, challenge_id)
    quiz: list[Quiz] = challenge.quiz
    return type


@app.post("/challenge/{challenge_id}/answer")
async def get_quiz(id: int, db: Session = Depends(get_db)):
    type = get_type(db, id)
    return type


# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
