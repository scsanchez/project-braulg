"""empty message

Revision ID: 5bde571c485e
Revises: 206b51f8fe16
Create Date: 2021-06-17 07:52:54.271809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5bde571c485e'
down_revision = '206b51f8fe16'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'chat', ['id'])
    op.create_unique_constraint(None, 'comments', ['id'])
    op.create_unique_constraint(None, 'message', ['id'])
    op.create_unique_constraint(None, 'post', ['id'])
    op.create_unique_constraint(None, 'share_trip', ['id'])
    op.create_unique_constraint(None, 'traveler', ['id'])
    op.create_unique_constraint(None, 'trip', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'trip', type_='unique')
    op.drop_constraint(None, 'traveler', type_='unique')
    op.drop_constraint(None, 'share_trip', type_='unique')
    op.drop_constraint(None, 'post', type_='unique')
    op.drop_constraint(None, 'message', type_='unique')
    op.drop_constraint(None, 'comments', type_='unique')
    op.drop_constraint(None, 'chat', type_='unique')
    # ### end Alembic commands ###
