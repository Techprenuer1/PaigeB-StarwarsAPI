"""empty message

Revision ID: 6fc98dc55d93
Revises: 77d364ac0c12
Create Date: 2023-06-15 00:54:39.286321

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6fc98dc55d93'
down_revision = '77d364ac0c12'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('hair_color', sa.String(length=80), nullable=True),
    sa.Column('eye_color', sa.String(length=80), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('mass', sa.Integer(), nullable=True),
    sa.Column('gender', sa.String(length=80), nullable=True),
    sa.Column('birth_year', sa.String(), nullable=True),
    sa.Column('skin_color', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('rotation_period', sa.Integer(), nullable=True),
    sa.Column('orbital_period', sa.Integer(), nullable=True),
    sa.Column('diameter', sa.Integer(), nullable=True),
    sa.Column('climate', sa.String(length=80), nullable=True),
    sa.Column('gravity', sa.String(length=80), nullable=True),
    sa.Column('terrain', sa.String(length=80), nullable=True),
    sa.Column('surface_water', sa.Integer(), nullable=True),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('model', sa.String(length=80), nullable=True),
    sa.Column('manufacturer', sa.String(length=80), nullable=True),
    sa.Column('cost_in_credits', sa.Integer(), nullable=True),
    sa.Column('length', sa.Integer(), nullable=True),
    sa.Column('max_atmosphering_speed', sa.Integer(), nullable=True),
    sa.Column('passengers', sa.Integer(), nullable=True),
    sa.Column('cargo_capacity', sa.Integer(), nullable=True),
    sa.Column('consumables', sa.String(length=80), nullable=True),
    sa.Column('vehicle_class', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vehicles')
    op.drop_table('planets')
    op.drop_table('characters')
    # ### end Alembic commands ###