import json
from sqlalchemy.orm import Session

from app.database.crud import get_move_by_id, get_pokemon_by_id, get_pokemon_by_name
from app.database.models import PokeMove


def create_seed_poke_move(db: Session):
    poke_moves = []
    for move_id in range(1, 901):
        # pokemon = get_pokemon_by_id(db, pokemon["types"][0]["type"]["name"])
        path = f"/home/yuuta/poke-move-api/data/data/moves/{move_id}.json"
        with open(path, "r") as f:
            move = json.load(f)
        # move = get_move_by_id(db, move["id"])
        if not get_move_by_id(db, move["id"]):
            continue
        pokemon_names = map(lambda x: x["name"], move["learned_by_pokemon"])
        skip_pokemon_ids = set()
        for name in pokemon_names:
            pokemon = get_pokemon_by_name(db, name)
            if pokemon == None:
                # print(pokemon, name)
                continue

            pokemon_id = pokemon.id
            skip_pokemon_ids.add(pokemon_id)
            # id pokemon-id	move-id	learn_probability can_learn
            poke_move = PokeMove(
                pokemon_id=pokemon_id,
                move_id=move_id,
                learn_probability=1,
                can_learn=True,
            )
            poke_moves.append(poke_move)

        for pokemon_id in range(1, 1011):
            if pokemon_id in skip_pokemon_ids:
                continue
            # id pokemon-id	move-id	learn_probability can_learn
            poke_move = PokeMove(
                pokemon_id=pokemon_id,
                move_id=move_id,
                learn_probability=0.5,
                can_learn=False,
            )
            poke_moves.append(poke_move)
    return poke_moves
