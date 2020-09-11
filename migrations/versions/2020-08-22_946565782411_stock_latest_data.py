"""stock latest data

Revision ID: 946565782411
Revises: f158a98be596
Create Date: 2020-08-22 02:23:29.548679

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "946565782411"
down_revision = "f158a98be596"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "stocks",
        sa.Column(
            "company_info", postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
    )
    op.add_column(
        "stocks",
        sa.Column(
            "latest_market_data", postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
    )
    op.drop_column("stocks", "info")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "stocks",
        sa.Column(
            "info",
            postgresql.JSONB(astext_type=sa.Text()),
            server_default=sa.text("'{}'::jsonb"),
            autoincrement=False,
            nullable=True,
        ),
    )
    op.drop_column("stocks", "latest_market_data")
    op.drop_column("stocks", "company_info")
    # ### end Alembic commands ###
