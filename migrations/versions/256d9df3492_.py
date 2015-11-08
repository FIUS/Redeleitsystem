"""empty message

Revision ID: 256d9df3492
Revises: bdf979c44e
Create Date: 2015-11-08 11:30:13.923165

"""

# revision identifiers, used by Alembic.
revision = '256d9df3492'
down_revision = 'bdf979c44e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('current_topic_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'events', 'topics', ['current_topic_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'events', type_='foreignkey')
    op.drop_column('events', 'current_topic_id')
    ### end Alembic commands ###
