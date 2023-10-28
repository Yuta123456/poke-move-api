from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from app.database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    api_token = Column(String, unique=True)
    refresh_token = Column(String, unique=True)

    challenges = relationship("Challenge", back_populates="user")


class Challenge(Base):
    __tablename__ = "challenges"

    id = Column(Integer, primary_key=True, index=True)
    is_answered = Column(Boolean)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="challenges")

    quiz = relationship("Quiz", back_populates="owner")


class Quiz(Base):
    __tablename__ = "quizzes"

    id = Column(Integer, primary_key=True, index=True)
    challenge_id = Column(Integer, ForeignKey("challenges.id"))
    pokemon_id = Column(Integer, ForeignKey("pokemons.id"))

    owner = relationship("Challenge", back_populates="quiz")

    quiz_answers = relationship("QuizAnswer", back_populates="quiz")
    quiz_choices = relationship("QuizChoice", back_populates="quiz")


class QuizAnswer(Base):
    __tablename__ = "quiz answers"
    id = Column(Integer, primary_key=True, index=True)
    quiz_id = Column(Integer, ForeignKey("quizzes.id"))
    move_id = Column(Integer, ForeignKey("moves.id"))

    quiz = relationship("Quiz", back_populates="quiz_answers")


class QuizChoice(Base):
    __tablename__ = "quiz choices"

    id = Column(Integer, primary_key=True, index=True)
    quiz_id = Column(Integer, ForeignKey("quizzes.id"))
    move_id = Column(Integer, ForeignKey("moves.id"))

    quiz = relationship("Quiz", back_populates="quiz_choices")


class Pokemon(Base):
    __tablename__ = "pokemons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type_id_1 = Column(Integer, ForeignKey("types.id"))
    type_id_2 = Column(Integer, ForeignKey("types.id"))
    img_url = Column(String)
    shiny_img_url = Column(String)


class Move(Base):
    __tablename__ = "moves"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type_id = Column(Integer, ForeignKey("types.id"))
    pp = Column(Integer)
    description = Column(String)


class PokeMove(Base):
    __tablename__ = "pokemoves"
    id = Column(Integer, primary_key=True, index=True)
    Pokemon_id = Column(Integer, ForeignKey("pokemons.id"))
    move_id = Column(Integer, ForeignKey("moves.id"))

    learn_probability = Column(Float)

    can_learn = Column(Boolean)


class Type(Base):
    __tablename__ = "types"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
