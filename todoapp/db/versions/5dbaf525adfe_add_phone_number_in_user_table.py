"""add phone number in user table

Revision ID: 5dbaf525adfe
Revises: 
Create Date: 2025-09-18 10:46:09.913673

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5dbaf525adfe'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('phone_number', sa.String(length=15), nullable=True))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'phone_number')
    pass
