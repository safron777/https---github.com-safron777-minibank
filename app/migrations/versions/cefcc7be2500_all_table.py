"""all table

Revision ID: cefcc7be2500
Revises: caaecf0dbb3f
Create Date: 2024-04-10 20:57:42.568707

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cefcc7be2500'
down_revision: Union[str, None] = 'caaecf0dbb3f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('feature_toggle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('feature_toggle', sa.BOOLEAN(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), sa.Identity(always=True, start=1), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('firstname', sa.String(), nullable=False),
    sa.Column('lastname', sa.String(), nullable=False),
    sa.Column('surname', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('feature_toggle')
    # ### end Alembic commands ###
