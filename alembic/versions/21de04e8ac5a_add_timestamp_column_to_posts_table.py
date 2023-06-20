"""add timestamp column to posts table

Revision ID: 21de04e8ac5a
Revises: df1fc8ae7204
Create Date: 2023-06-19 20:26:23.297336

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '21de04e8ac5a'
down_revision = 'df1fc8ae7204'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'created_at')
    pass
