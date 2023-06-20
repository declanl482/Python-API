"""add user table

Revision ID: 12e01e8b3783
Revises: 21de04e8ac5a
Create Date: 2023-06-19 20:38:02.681618

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '12e01e8b3783'
down_revision = '21de04e8ac5a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users', 
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
