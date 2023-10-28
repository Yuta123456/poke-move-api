import json
from sqlalchemy.orm import Session
import sys

# import os

from app.database.models import Pokemon
from app.database.crud import get_type_by_name


# pokemon
# id = Column(Integer, primary_key=True, index=True)
# name = Column(String)
# type_id_1 = Column(Integer, ForeignKey("types.id"))
# type_id_2 = Column(Integer, ForeignKey("types.id"))
# img_url = Column(String)
# shiny_img_url = Column(String)
def create_seed_pokemon(db: Session) -> list[Pokemon]:
    pokemons = []
    # for i in range(1, 1011):
    for i in range(1, 1011):
        # /home/yuuta/poke-move-api/data/data/pokemons/1008.json
        path = f"/home/yuuta/poke-move-api/data/data/pokemons/{i}.json"
        with open(path, "r") as f:
            pokemon = json.load(f)
        name = pokemon["name"]
        type_id_1 = get_type_by_name(db, pokemon["types"][0]["type"]["name"]).id

        if len(pokemon["types"]) > 1:
            type_id_2 = get_type_by_name(db, pokemon["types"][1]["type"]["name"]).id
        else:
            type_id_2 = get_type_by_name(db, "none").id
        img_url = pokemon["sprites"]["front_default"]
        shiny_img_url = pokemon["sprites"]["front_shiny"]
        # print(
        #     type(i),
        #     type(name),
        #     type(type_id_1),
        #     type(type_id_2),
        #     type(img_url),
        #     type(shiny_img_url),
        # )
        # print(
        #     i,
        #     name,
        #     type_id_1,
        #     type_id_2,
        #     img_url,
        #     shiny_img_url,
        # )
        pokemon = Pokemon(
            id=i,
            name=name,
            type_id_1=type_id_1,
            type_id_2=type_id_2,
            img_url=img_url,
            shiny_img_url=shiny_img_url,
        )
        pokemons.append(pokemon)
    return pokemons
