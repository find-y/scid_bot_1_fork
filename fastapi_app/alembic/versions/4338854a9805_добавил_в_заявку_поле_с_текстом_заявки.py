"""Добавил в заявку поле с текстом заявки

Revision ID: 4338854a9805
Revises: b27a622adf51
Create Date: 2024-10-01 14:16:39.333260

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "4338854a9805"
down_revision: Union[str, None] = "b27a622adf51"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("contactrequest", schema=None) as batch_op:
        batch_op.add_column(sa.Column("text", sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("contactrequest", schema=None) as batch_op:
        batch_op.drop_column("text")

    # ### end Alembic commands ###
