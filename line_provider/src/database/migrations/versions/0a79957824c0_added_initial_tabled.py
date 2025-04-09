"""Added initial tabled

Revision ID: 0a79957824c0
Revises: 
Create Date: 2025-04-07 16:42:39.571421

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '0a79957824c0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('events',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('coefficient', sa.NUMERIC(precision=10, scale=2), autoincrement=False, nullable=False),
    sa.Column('deadline', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('status', postgresql.ENUM('NEW', 'FINISHED_WIN', 'FINISHED_LOSE', name='eventstatus'), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.CheckConstraint('coefficient > 0::numeric', name='ck_coefficient_positive'),
    sa.PrimaryKeyConstraint('id', name='events_pkey')
    )


def downgrade() -> None:
    op.drop_table('events')