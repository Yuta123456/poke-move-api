from sqlalchemy.orm import Session

from app.database.models import Challenge, Type, Pokemon
from app.database.schemas import User

# from database.models import Item, User
# from database.schemas import ItemCreate, UserCreate


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_type(db: Session, type_id: int):
    return db.query(Type).filter(Type.id == type_id).first()


def get_challenge_by_id(db: Session, challenge_id: int):
    return db.query(Challenge).filter(Challenge.id == challenge_id).first()


def get_type_by_name(db: Session, type_name: str):
    return db.query(Type).filter(Type.name == type_name).first()


def get_pokemon_by_id(db: Session, pokemon_id: str):
    return db.query(Pokemon).filter(Pokemon.id == pokemon_id).first()


def get_pokemon_by_name(db: Session, pokemon_name: str):
    return db.query(Pokemon).filter(Pokemon.name == pokemon_name).first()
