"""Add models

Revision ID: d946b3625d60
Revises: 
Create Date: 2024-09-03 15:08:32.720289

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd946b3625d60'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'DetMir',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('image_url', sa.String(), nullable=False),
        sa.Column('content_url', sa.String(), nullable=False),
        sa.Column('meta', sa.String(), nullable=False),
        sa.Column('place', sa.Integer(), nullable=False),
        sa.Column('position', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'product',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('price', sa.Float(), nullable=False),
        sa.Column('price_sale', sa.Float(), nullable=False),
        sa.Column('description', sa.String(), nullable=False),
        sa.Column('code', sa.String(), nullable=False),
        sa.Column('images', sa.String(), nullable=False),
        sa.Column('comment_count', sa.Integer(), nullable=False),
        sa.Column('rating', sa.Float(), nullable=False),
        sa.Column('brand', sa.String(), nullable=False),
        sa.Column('categories', sa.String(), nullable=False),
        sa.Column('content_url', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('product')
    op.drop_table('DetMir')
