"""empty message

Revision ID: 579c9c7756
Revises: 546e34fac4
Create Date: 2015-11-13 16:17:22.756119

"""

# revision identifiers, used by Alembic.
revision = '579c9c7756'
down_revision = '546e34fac4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('topics_name_key', 'topics', type_='unique')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('topics_name_key', 'topics', ['name'])
    ### end Alembic commands ###
