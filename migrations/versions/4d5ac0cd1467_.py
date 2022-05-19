"""empty message

Revision ID: 4d5ac0cd1467
Revises: 86f26149ff1e
Create Date: 2022-05-19 19:12:13.905934

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4d5ac0cd1467'
down_revision = '86f26149ff1e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('character_ibfk_1', 'character', type_='foreignkey')
    op.drop_column('character', 'favorited_by')
    op.drop_constraint('planet_ibfk_1', 'planet', type_='foreignkey')
    op.drop_column('planet', 'favorited_by')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('planet', sa.Column('favorited_by', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('planet_ibfk_1', 'planet', 'user', ['favorited_by'], ['id'])
    op.add_column('character', sa.Column('favorited_by', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('character_ibfk_1', 'character', 'user', ['favorited_by'], ['id'])
    # ### end Alembic commands ###
