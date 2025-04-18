"""add image to food_items

Revision ID: f0f222654c78
Revises: a3b6ecacce3d
Create Date: 2025-04-14 12:56:31.084817

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0f222654c78'
down_revision = 'a3b6ecacce3d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('food_items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('food_items', schema=None) as batch_op:
        batch_op.drop_column('image')

    # ### end Alembic commands ###
