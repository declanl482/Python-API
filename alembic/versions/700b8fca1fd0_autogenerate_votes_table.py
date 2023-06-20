"""autogenerate votes table

Revision ID: 700b8fca1fd0
Revises: d74ab1420c50
Create Date: 2023-06-19 21:08:53.467414

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '700b8fca1fd0'
down_revision = 'd74ab1420c50'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('votes')
    # ### end Alembic commands ###