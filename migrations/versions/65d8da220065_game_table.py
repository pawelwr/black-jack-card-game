"""game table

Revision ID: 65d8da220065
Revises: 
Create Date: 2019-12-02 12:32:20.503245

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65d8da220065'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('deck', sa.String(), nullable=True),
    sa.Column('pc_cards', sa.String(length=20), nullable=True),
    sa.Column('p1_cards', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('game')
    # ### end Alembic commands ###