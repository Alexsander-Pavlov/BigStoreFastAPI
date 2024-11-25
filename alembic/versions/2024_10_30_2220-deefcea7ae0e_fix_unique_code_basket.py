"""fix unique_code basket

Revision ID: deefcea7ae0e
Revises: fb5a0ab49610
Create Date: 2024-10-30 22:20:11.119319

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "deefcea7ae0e"
down_revision: Union[str, None] = "fb5a0ab49610"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("baskets", sa.Column("coupon_id", sa.Integer(), nullable=True))
    op.create_foreign_key(None, "baskets", "coupons", ["coupon_id"], ["id"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "baskets", type_="foreignkey")
    op.drop_column("baskets", "coupon_id")
    # ### end Alembic commands ###
