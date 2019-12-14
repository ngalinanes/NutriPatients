"""empty message

Revision ID: c267e9562021
Revises: 4fe29475cec1
Create Date: 2019-12-13 21:34:01.588093

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c267e9562021'
down_revision = '4fe29475cec1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('actividad_fisica',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('actividad', sa.String(length=30), nullable=True),
    sa.Column('cual_actividad', sa.String(length=60), nullable=True),
    sa.Column('cuantas_veces', sa.String(length=80), nullable=True),
    sa.Column('paciente_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['paciente_id'], ['pacientes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_actividad_fisica_actividad'), 'actividad_fisica', ['actividad'], unique=False)
    op.create_index(op.f('ix_actividad_fisica_cual_actividad'), 'actividad_fisica', ['cual_actividad'], unique=False)
    op.create_index(op.f('ix_actividad_fisica_cuantas_veces'), 'actividad_fisica', ['cuantas_veces'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_actividad_fisica_cuantas_veces'), table_name='actividad_fisica')
    op.drop_index(op.f('ix_actividad_fisica_cual_actividad'), table_name='actividad_fisica')
    op.drop_index(op.f('ix_actividad_fisica_actividad'), table_name='actividad_fisica')
    op.drop_table('actividad_fisica')
    # ### end Alembic commands ###
