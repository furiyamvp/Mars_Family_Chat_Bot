"""empty message

Revision ID: 8922be2f6251
Revises: 
Create Date: 2024-10-09 19:09:35.676763

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8922be2f6251'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employee',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('chat_id', sa.BigInteger(), nullable=True),
    sa.Column('phone_number', sa.String(), nullable=True),
    sa.Column('role', sa.Enum('admin', 'moderator', name='employeerole'), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('forbidden_word',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('word', sa.String(), nullable=False),
    sa.Column('answer', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('employee_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('forbidden_word')
    op.drop_table('employee')
    # ### end Alembic commands ###
