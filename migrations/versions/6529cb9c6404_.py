"""empty message

Revision ID: 6529cb9c6404
Revises: da2f0585907e
Create Date: 2021-07-05 21:42:17.369720

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6529cb9c6404'
down_revision = 'da2f0585907e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'post', ['id'])
    op.create_unique_constraint(None, 'shared_trip', ['id'])
    op.create_unique_constraint(None, 'traveler', ['id'])
    op.create_unique_constraint(None, 'trip', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'trip', type_='unique')
    op.drop_constraint(None, 'traveler', type_='unique')
    op.drop_constraint(None, 'shared_trip', type_='unique')
    op.drop_constraint(None, 'post', type_='unique')
    # ### end Alembic commands ###