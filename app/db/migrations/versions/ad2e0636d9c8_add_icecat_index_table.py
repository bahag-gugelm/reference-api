"""add icecat_index table

Revision ID: ad2e0636d9c8
Revises: 54cc68069f12
Create Date: 2022-06-09 07:40:01.192873

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad2e0636d9c8'
down_revision = '54cc68069f12'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('icecat_index',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sku', sa.String(length=100), nullable=False),
    sa.Column('brand', sa.String(length=100), nullable=False),
    sa.Column('ean', sa.String(length=5000), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('icecat_index')
    # ### end Alembic commands ###
