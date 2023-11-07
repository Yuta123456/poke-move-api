import random
import secrets
from sqlalchemy.orm import Session

from app.database.models import Challenge, Quiz, User, QuizAnswer, QuizChoice
from app.database.crud import (
    get_answer_by_challenge_id,
    get_learned_moves_by_pokemon_id,
    get_not_learned_moves_by_pokemon_id,
    update_challenge_is_answered,
)
from app.database.schemas import UserAnswer


def create_challenge(db: Session, user: User) -> Challenge:
    # challengeが勝手に回答されたら困るので、推測不可能なid
    challenge_id = secrets.token_hex(32)
    challenge = Challenge(
        id=challenge_id, is_answered=False, user_id=user.id, user=user
    )
    db.add(challenge)
    db.commit()
    create_quiz(db, challenge)
    return challenge


def create_quiz(db: Session, challenge: Challenge) -> Quiz:
    quizzes = []

    for _ in range(5):
        pokemon_id = random.randint(1, 1011)
        quiz = Quiz(challenge_id=challenge.id, pokemon_id=pokemon_id)
        quizzes.append(quiz)

        # クイズ生成
        pokemon_learned_moves = get_learned_moves_by_pokemon_id(db, pokemon_id)
        answer_move = random.sample(pokemon_learned_moves, 1)
        pokemon_not_learned_moves = get_not_learned_moves_by_pokemon_id(db, pokemon_id)
        question_move = random.sample(pokemon_not_learned_moves, 3)

        for choice in answer_move + question_move:
            quiz_choice = QuizChoice(quiz_id=quiz.id, move_id=choice.id, quiz=quiz)
            db.add(quiz_choice)
        quiz_answer = QuizAnswer(quiz_id=quiz.id, move_id=answer_move[0].id, quiz=quiz)
        db.add(quiz_answer)
    db.add_all(quizzes)
    db.commit()


def check_answer(db: Session, challenge_id: str, user_answer: UserAnswer):
    answers = get_answer_by_challenge_id(db, challenge_id)
    # quiz_id: int
    # answer_move_id: int
    score = 0
    user_answers = sorted(user_answer.answers, key=lambda x: x.quiz_id)
    for i in range(len(user_answers)):
        if user_answers[i].answer_move_id == answers[i].move_id:
            score += 1
    update_challenge_is_answered(db, challenge_id)
    return {"answers": answers, "score": score}
