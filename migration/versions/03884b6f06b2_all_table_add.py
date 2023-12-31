"""all_table_add

Revision ID: 03884b6f06b2
Revises: 1c10d28d7c92
Create Date: 2023-10-28 18:37:06.188622

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '03884b6f06b2'
down_revision: Union[str, None] = '1c10d28d7c92'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('api_token', sa.String(), nullable=True),
    sa.Column('refresh_token', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('api_token'),
    sa.UniqueConstraint('refresh_token')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('challenges',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_answered', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_challenges_id'), 'challenges', ['id'], unique=False)
    op.create_table('quizzes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('challenge_id', sa.Integer(), nullable=True),
    sa.Column('pokemon_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['challenge_id'], ['challenges.id'], ),
    sa.ForeignKeyConstraint(['pokemon_id'], ['pokemons.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_quizzes_id'), 'quizzes', ['id'], unique=False)
    op.create_table('quiz answers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quiz_id', sa.Integer(), nullable=True),
    sa.Column('move_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['move_id'], ['moves.id'], ),
    sa.ForeignKeyConstraint(['quiz_id'], ['quizzes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_quiz answers_id'), 'quiz answers', ['id'], unique=False)
    op.create_table('quiz choices',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quiz_id', sa.Integer(), nullable=True),
    sa.Column('move_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['move_id'], ['moves.id'], ),
    sa.ForeignKeyConstraint(['quiz_id'], ['quizzes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_quiz choices_id'), 'quiz choices', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_quiz choices_id'), table_name='quiz choices')
    op.drop_table('quiz choices')
    op.drop_index(op.f('ix_quiz answers_id'), table_name='quiz answers')
    op.drop_table('quiz answers')
    op.drop_index(op.f('ix_quizzes_id'), table_name='quizzes')
    op.drop_table('quizzes')
    op.drop_index(op.f('ix_challenges_id'), table_name='challenges')
    op.drop_table('challenges')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
