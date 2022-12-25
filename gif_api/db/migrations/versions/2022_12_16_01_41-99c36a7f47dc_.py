"""empty message

Revision ID: 99c36a7f47dc
Revises: 
Create Date: 2022-12-16 01:41:34.028846

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = "99c36a7f47dc"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "gif",
        sa.Column(
            "gif_id",
            postgresql.UUID(as_uuid=True),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column("title", sa.String(length=127), nullable=False),
        sa.Column("url", sa.String(length=255), nullable=False),
        sa.Column(
            "rating",
            sa.Enum("Y", "G", "PG", "PG13", "R", name="gifrating"),
            server_default="G",
            nullable=False,
        ),
        sa.Column(
            "create_datetime",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "update_datetime",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("gif_id"),
        sa.UniqueConstraint("gif_id"),
        sa.UniqueConstraint("url"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("gif")
    # ### end Alembic commands ###
