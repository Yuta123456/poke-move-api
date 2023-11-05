from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
import os


sys.path.append("./")
sys.path.append("../")
from migration.seed.move import create_seed_moves
from migration.seed.type import get_seed_types
from migration.seed.pokemon import create_seed_pokemon
from migration.seed.poke_move import create_seed_poke_move

from app.database.models import Pokemon, Type

# データベース接続情報
db_url = "postgresql://postgres:postgres@localhost:54322/postgres"

# SQLAlchemyエンジンの作成
engine = create_engine(db_url)

# セッションの作成
Session = sessionmaker(bind=engine)
session = Session()

# add types
types = get_seed_types()
# session.add_all(types)
session.commit()

# add pokemons
pokemons = create_seed_pokemon(session)
moves = create_seed_moves(session)

# session.add_all(pokemons)
# session.add_all(moves)
session.commit()

poke_moves = create_seed_poke_move(session)
print(len(poke_moves))
session.add_all(poke_moves)
session.commit()
