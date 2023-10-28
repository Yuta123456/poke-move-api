from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
import os

sys.path.append("app")

from database.models import Type

# データベース接続情報
db_url = "postgresql://postgres:postgres@localhost:54322/postgres"

# SQLAlchemyエンジンの作成
engine = create_engine(db_url)

# セッションの作成
Session = sessionmaker(bind=engine)
session = Session()

# 初期データの挿入
data = [
    Type(name="Fire"),
    Type(name="Water"),
    Type(name="Grass"),
    Type(name="Electric"),
    Type(name="Ice"),
    Type(name="Fighting"),
    Type(name="Poison"),
    Type(name="Ground"),
    Type(name="Flying"),
    Type(name="Psychic"),
    Type(name="Bug"),
    Type(name="Rock"),
    Type(name="Ghost"),
    Type(name="Dragon"),
    Type(name="Dark"),
    Type(name="Steel"),
    Type(name="Fairy"),
    # 他の初期データも追加
]
session.add_all(data)
session.commit()
