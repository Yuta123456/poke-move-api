import secrets
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
import jwt
import os
from sqlalchemy.orm import Session
import uuid
from app.database.models import User
from app.database.crud import get_user_by_id

SECRET_KEY = os.environ["SECRET_KEY"]
ALGORITHM = os.environ["ALGORITHM"]

ACCESS_TOKEN_EXPIRE_MINUTES = 60
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def generate_user_id():
    return str(uuid.uuid4())


def generate_refresh_token():
    return secrets.token_hex(32)


# アクセストークンの発行関数
def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expires = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expires})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# アクセストークンの検証
def verify_access_token(encoded_token: str = Depends(oauth2_scheme)):
    try:
        # アクセストークンの検証
        payload = jwt.decode(encoded_token, SECRET_KEY, algorithms=[ALGORITHM])
        # 有効期限の確認
        if datetime.utcfromtimestamp(payload["exp"]) < datetime.utcnow():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="アクセストークンの有効期限が切れています",
                headers={"WWW-Authenticate": "Bearer"},
            )
        user_id = payload["sub"]

        return user_id  # 正当なアクセストークン
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="アクセストークンが無効です",
            headers={"WWW-Authenticate": "Bearer"},
        )


def create_user(db: Session) -> User:
    user_id = generate_user_id()
    expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user_id}, expires_delta=expires_delta
    )
    refresh_token = generate_refresh_token()
    user = User(id=user_id, api_token=access_token, refresh_token=refresh_token)
    # user追加
    db.add(user)
    db.commit()
    return user
