from pydantic import BaseModel


class Answer(BaseModel):
    quiz_id: int
    answer_move_id: int


class UserAnswer(BaseModel):
    challenge_id: str
    answers: list[Answer]
