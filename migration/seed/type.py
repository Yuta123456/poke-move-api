from app.database.models import Type


def get_seed_types():
    return [
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
