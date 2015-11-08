"""empty message

Revision ID: 3c75c74bb94
Revises: 256d9df3492
Create Date: 2015-11-08 13:06:23.520483

"""

# revision identifiers, used by Alembic.
revision = '3c75c74bb94'
down_revision = '256d9df3492'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('events_current_topic_id_fkey', 'events', type_='foreignkey')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('events_current_topic_id_fkey', 'events', 'topics', ['current_topic_id'], ['id'])
    ### end Alembic commands ###