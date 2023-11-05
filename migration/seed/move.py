import json
from sqlalchemy.orm import Session
import sys

# import os

from app.database.models import Move
from app.database.crud import get_type_by_name


def create_seed_moves(db: Session) -> list[Move]:
    moves = []
    for i in range(1, 901):
        path = f"/home/yuuta/poke-move-api/data/data/moves/{i}.json"
        with open(path, "r") as f:
            move = json.load(f)

        description_list = list(
            filter(lambda x: x["language"]["name"] == "ja", move["flavor_text_entries"])
        )
        if len(description_list) == 0:
            continue
        description = description_list[0]["flavor_text"]
        name = move["name"]
        type_id = get_type_by_name(db, move["type"]["name"]).id
        pp = move["pp"]
        move = Move(id=i, name=name, type_id=type_id, description=description, pp=pp)
        # print(i, name, type_id, description, pp)
        moves.append(move)
    return moves
