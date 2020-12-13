"""empty message

Revision ID: 852240cf4dc7
Revises: e8267c01edfe
Create Date: 2020-12-13 09:35:17.871312

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '852240cf4dc7'
down_revision = 'e8267c01edfe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'user', 'siswa', ['user_name'], ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    # ### end Alembic commands ###