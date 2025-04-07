"""Added initial tabled

Revision ID: 50d9f3cae279
Revises: 
Create Date: 2025-04-07 15:13:14.570435

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '50d9f3cae279'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('bets',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('status', postgresql.ENUM('PENDING', 'WIN', 'LOSE', name='betstatus'), autoincrement=False, nullable=False),
    sa.Column('sum', sa.NUMERIC(), autoincrement=False, nullable=False),
    sa.Column('event_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='bets_pkey')
    )


def downgrade() -> None:
    op.drop_table('bets')