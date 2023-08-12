from enum import Enum
from fastapi import FastAPI, HTTPException

app = FastAPI()


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
async def root(level: str):
    print(level, Level.HIGH.value)
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
