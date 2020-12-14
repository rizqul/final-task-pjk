"""empty message

Revision ID: dd6b071eb4ab
Revises: b962f40c4cc6
Create Date: 2020-12-14 10:44:33.116142

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'dd6b071eb4ab'
down_revision = 'b962f40c4cc6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sa.String(length=128), nullable=False))
    op.drop_column('user', 'passsword')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('passsword', mysql.VARCHAR(length=128), nullable=False))
    op.drop_column('user', 'password')
    # ### end Alembic commands ###