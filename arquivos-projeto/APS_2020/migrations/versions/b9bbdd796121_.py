"""empty message

Revision ID: b9bbdd796121
Revises: 
Create Date: 2020-05-15 17:46:28.801220

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9bbdd796121'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('noticias',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('link', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('link')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('noticias')
    # ### end Alembic commands ###
