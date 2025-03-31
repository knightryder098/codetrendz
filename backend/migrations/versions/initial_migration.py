"""Initial migration

Revision ID: 1
Create Date: 2024-03-31 19:45:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSON

# revision identifiers, used by Alembic.
revision = '1'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'repositories',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('full_name', sa.String(length=255), nullable=False),
        sa.Column('description', sa.String(length=1000)),
        sa.Column('html_url', sa.String(length=255)),
        sa.Column('stars', sa.Integer(), default=0),
        sa.Column('language_stats', JSON),
        sa.Column('last_analyzed', sa.DateTime()),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('full_name')
    )

def downgrade():
    op.drop_table('repositories') 