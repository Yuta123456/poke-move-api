"""integer to String

Revision ID: 6807c65bb79d
Revises: a6b2cf8c2c51
Create Date: 2023-11-05 16:36:18.301134

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "6807c65bb79d"
down_revision: Union[str, None] = "a6b2cf8c2c51"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_constraint("quizzes_challenge_id_fkey", "quizzes", type_="foreignkey")
    op.drop_constraint("quizzes_challenge_id_fkey", "quizzes", type_="foreignkey")
    op.drop_constraint("challenges_user_id_fkey", "challenges", type_="foreignkey")

    op.alter_column(
        "quizzes",
        "challenge_id",
        existing_type=sa.INTEGER(),
        type_=sa.String(),
        existing_nullable=True,
    )
    op.alter_column(
        "challenges",
        "id",
        existing_type=sa.INTEGER(),
        type_=sa.String(),
        existing_nullable=False,
        existing_server_default=sa.text("nextval('challenges_id_seq'::regclass)"),
    )
    op.alter_column(
        "challenges",
        "user_id",
        existing_type=sa.INTEGER(),
        type_=sa.String(),
        existing_nullable=True,
    )

    op.alter_column(
        "users",
        "id",
        existing_type=sa.INTEGER(),
        type_=sa.String(),
        existing_nullable=False,
    )
    op.create_foreign_key(
        "quizzes_challenge_id_fkey", "quizzes", "challenges", ["challenge_id"], ["id"]
    )
    op.create_foreign_key(
        "challenges_user_id_fkey", "challenges", "users", ["user_id"], ["id"]
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "users",
        "id",
        existing_type=sa.String(),
        type_=sa.INTEGER(),
        existing_nullable=False,
    )
    op.alter_column(
        "quizzes",
        "challenge_id",
        existing_type=sa.String(),
        type_=sa.INTEGER(),
        existing_nullable=True,
    )
    op.alter_column(
        "challenges",
        "user_id",
        existing_type=sa.String(),
        type_=sa.INTEGER(),
        existing_nullable=True,
    )
    op.alter_column(
        "challenges",
        "id",
        existing_type=sa.String(),
        type_=sa.INTEGER(),
        existing_nullable=False,
        existing_server_default=sa.text("nextval('challenges_id_seq'::regclass)"),
    )
    # ### end Alembic commands ###