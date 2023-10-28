from dotenv import load_dotenv

from app.database.crud import get_type

load_dotenv()
import sys
import os

sys.path.append("app")
from enum import Enum
from fastapi import Depends, FastAPI, HTTPException

# from database.crud import create_user

from database.main import Base, SessionLocal, engine
from sqlalchemy.orm import Session

from database.schemas import UserCreate

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


@app.get("/create")
async def create(email: str, db: Session = Depends(get_db)):
    user = UserCreate(email=email, password="password")
    create_user(db, user=user)


@app.get("/type/{id}")
async def type(id: int, db: Session = Depends(get_db)):
    type = get_type(db, id)
    return type


# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
