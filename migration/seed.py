from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
import os

sys.path.append("./")
sys.path.append("../")

from migration.seed.pokemon import create_seed_pokemon

from app.database.models import Pokemon, Type

# データベース接続情報
db_url = "postgresql://postgres:postgres@localhost:54322/postgres"

# SQLAlchemyエンジンの作成
engine = create_engine(db_url)

# セッションの作成
Session = sessionmaker(bind=engine)
session = Session()

# add types
types = [
    Type(name="normal"),
    Type(name="fire"),
    Type(name="water"),
    Type(name="grass"),
    Type(name="electric"),
    Type(name="ice"),
    Type(name="fighting"),
    Type(name="poison"),
    Type(name="ground"),
    Type(name="flying"),
    Type(name="psychic"),
    Type(name="bug"),
    Type(name="rock"),
    Type(name="ghost"),
    Type(name="dragon"),
    Type(name="dark"),
    Type(name="steel"),
    Type(name="fairy"),
    Type(name="none"),
]
session.add_all(types)
session.commit()

# add pokemons
pokemons = create_seed_pokemon(session)
# 1 bulbasaur 127 131 https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/1.png

# pokemon = Pokemon(
#     id=2,
#     name="bulbasaur",
#     type_id_1=127,
#     type_id_2=131,
#     img_url="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
#     shiny_img_url="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/1.png",
# )

session.add_all(pokemons)
session.commit()
