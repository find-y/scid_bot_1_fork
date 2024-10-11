"""Изменил оценку на целочисленное

Revision ID: 5ee7c0cb24c0
Revises: 0f589c365de8
Create Date: 2024-09-28 22:01:11.787557
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "5ee7c0cb24c0"
down_revision: Union[str, None] = "0f589c365de8"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("review", schema=None) as batch_op:
        batch_op.alter_column(
            "rating",
            existing_type=sa.DOUBLE_PRECISION(precision=53),
            type_=sa.Integer(),
            existing_nullable=False,
        )

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("review", schema=None) as batch_op:
        batch_op.alter_column(
            "rating",
            existing_type=sa.Integer(),
            type_=sa.DOUBLE_PRECISION(precision=53),
            existing_nullable=False,
        )

    # ### end Alembic commands ###
