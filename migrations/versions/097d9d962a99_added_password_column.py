"""Added password column

Revision ID: 097d9d962a99
Revises: 
Create Date: 2021-06-16 03:19:18.431964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '097d9d962a99'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('URL', sa.Column('password', sa.String(length=60), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('URL', 'password')
    # ### end Alembic commands ###