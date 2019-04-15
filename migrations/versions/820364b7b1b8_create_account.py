"""Create Account

Revision ID: 820364b7b1b8
Revises: 
Create Date: 2019-04-14 22:55:48.212725

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "820364b7b1b8"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "accounts",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("email", sa.Text(), unique=True, nullable=False),
        sa.Column("country", sa.Text(), nullable=False),
        sa.Column("default_currency", sa.Text(), nullable=False),
    )


def downgrade():
    op.drop_table("accounts")
