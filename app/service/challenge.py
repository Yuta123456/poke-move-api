import secrets
from sqlalchemy.orm import Session

from app.database.models import Challenge, User


def create_challenge(db: Session, user: User) -> Challenge:
    challenge_id = secrets.token_hex(32)
    challenge = Challenge(
        id=challenge_id, is_answered=False, user_id=user.id, user=user
    )
    db.add(challenge)
    return challenge
