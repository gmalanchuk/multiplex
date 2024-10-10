"""empty message

Revision ID: b28d48d98af1
Revises: 
Create Date: 2024-10-10 17:28:10.037506

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b28d48d98af1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movies',
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('age_category', sa.Integer(), nullable=False),
    sa.Column('release_year', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_movies_created_at'), 'movies', ['created_at'], unique=False)
    op.create_index(op.f('ix_movies_id'), 'movies', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_movies_id'), table_name='movies')
    op.drop_index(op.f('ix_movies_created_at'), table_name='movies')
    op.drop_table('movies')
    # ### end Alembic commands ###