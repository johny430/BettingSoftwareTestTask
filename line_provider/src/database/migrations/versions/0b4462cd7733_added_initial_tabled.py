"""Added initial tabled

Revision ID: 0b4462cd7733
Revises: 
Create Date: 2025-04-07 10:33:54.826265

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '0b4462cd7733'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None





def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bets',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('state', postgresql.ENUM('WIN', 'LOSE', 'PENDING', name='betstate'), autoincrement=False, nullable=False),
    sa.Column('sum', sa.NUMERIC(), autoincrement=False, nullable=False),
    sa.Column('event_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='bets_pkey')
    )
    op.create_table('events',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('coefficient', sa.NUMERIC(precision=10, scale=2), autoincrement=False, nullable=False),
    sa.Column('deadline', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('state', postgresql.ENUM('NEW', 'FINISHED_WIN', 'FINISHED_LOSE', name='eventstate'), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.CheckConstraint('coefficient > 0::numeric', name='ck_coefficient_positive'),
    sa.PrimaryKeyConstraint('id', name='events_pkey')
    )
    # ### end Alembic commands ###

def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('events')
    op.drop_table('bets')
    # ### end Alembic commands ###