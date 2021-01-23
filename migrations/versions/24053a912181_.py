"""empty message

Revision ID: 24053a912181
Revises: 
Create Date: 2021-01-23 10:09:35.308020

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24053a912181'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('URL',
    sa.Column('short_url', sa.String(length=50), nullable=False),
    sa.Column('redirect_url', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('short_url')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('URL')
    # ### end Alembic commands ###