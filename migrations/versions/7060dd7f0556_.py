"""empty message

Revision ID: 7060dd7f0556
Revises: b105fdbc21c7
Create Date: 2019-02-23 11:26:25.311402

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7060dd7f0556'
down_revision = 'b105fdbc21c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('questions_level2',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('language', sa.String(), nullable=True),
    sa.Column('question_display_id', sa.Integer(), nullable=True),
    sa.Column('question', sa.String(), nullable=True),
    sa.Column('answer', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('questions_level2')
    # ### end Alembic commands ###
