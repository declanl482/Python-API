"""add foreign-key to posts table

Revision ID: d74ab1420c50
Revises: 12e01e8b3783
Create Date: 2023-06-19 20:54:54.395533

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd74ab1420c50'
down_revision = '12e01e8b3783'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fkey', source_table='posts', referent_table='users',local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fkey', table_name='posts')
    op.drop_column('owner_id')
    pass
