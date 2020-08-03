"""empty message

Revision ID: 2a42400b31f0
Revises: 8a0929a6fa45
Create Date: 2020-08-03 13:14:30.523230

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a42400b31f0'
down_revision = '8a0929a6fa45'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recruits', sa.Column('rocketchat_user', sa.String(length=100), nullable=True))
    op.drop_column('recruits', 'chatname')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recruits', sa.Column('chatname', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.drop_column('recruits', 'rocketchat_user')
    # ### end Alembic commands ###