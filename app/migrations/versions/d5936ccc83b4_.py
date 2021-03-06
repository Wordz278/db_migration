"""empty message

Revision ID: d5936ccc83b4
Revises: b29286d67068
Create Date: 2020-08-03 05:41:46.751443

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5936ccc83b4'
down_revision = 'b29286d67068'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recruits', sa.Column('cohort', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('recruits', 'cohort')
    # ### end Alembic commands ###
