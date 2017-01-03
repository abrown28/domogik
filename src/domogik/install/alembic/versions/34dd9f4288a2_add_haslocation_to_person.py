"""Add hasLocation to person

Revision ID: 34dd9f4288a2
Revises: cecc475b4f95
Create Date: 2017-01-01 06:40:44.581142

"""

# revision identifiers, used by Alembic.
revision = '34dd9f4288a2'
down_revision = 'cecc475b4f95'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('core_person', sa.Column('location_sensor', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'core_person', 'core_sensor', ['location_sensor'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'core_person', type_='foreignkey')
    op.drop_column('core_person', 'location_sensor')
    ### end Alembic commands ###