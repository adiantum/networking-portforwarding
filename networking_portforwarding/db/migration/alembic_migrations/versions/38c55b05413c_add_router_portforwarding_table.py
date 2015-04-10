# Copyright 2014 OpenStack Foundation
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


"""Add router portforwarding capabilities

Revision ID: 38c55b05413c
Revises: juno
Create Date: 2014-08-26 16:52:19.478696

"""

# revision identifiers, used by Alembic.
revision = '38c55b05413c'
down_revision = '51c54792158e'

# Change to ['*'] if this migration applies to all plugins

migration_for_plugins = [
    'neutron.plugins.ml2.plugin.Ml2Plugin'
]

from alembic import op
import sqlalchemy as sa


def upgrade(active_plugins=None, options=None):
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('portforwardingrules',
        sa.Column('tenant_id', sa.String(length=255), nullable=True),
        sa.Column('id', sa.String(length=36), nullable=False),
        sa.Column('router_id', sa.String(length=36), nullable=True),
        sa.Column('outside_port', sa.Integer(), nullable=True),
        sa.Column('inside_addr', sa.String(length=15), nullable=True),
        sa.Column('inside_port', sa.Integer(), nullable=True),
        sa.Column('protocol', sa.String(length=4), nullable=True),
        sa.ForeignKeyConstraint(['router_id'], ['routers.id'],
                                ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('router_id', 'protocol', 'outside_port',
                            name='outside_port')
                    )
    ### end Alembic commands ###


def downgrade(active_plugins=None, options=None):
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('portforwardingrules')
    ### end Alembic commands ###
