"""empty message

Revision ID: 9c891845f023
Revises: 0ab69af194b3
Create Date: 2020-05-15 18:05:35.061092

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c891845f023'
down_revision = '0ab69af194b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('noticias',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('link', sa.String(), nullable=True),
    sa.Column('titulo', sa.String(), nullable=True),
    sa.Column('data', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('link')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('noticias')
    # ### end Alembic commands ###