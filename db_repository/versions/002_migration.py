from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
users = Table('users', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=64)),
    Column('email', String(length=120)),
    Column('password', String(length=120)),
    Column('first_name', String(length=120)),
    Column('last_name', String(length=120)),
    Column('other_name', String(length=120)),
    Column('role', Integer),
    Column('verified', Integer),
    Column('department', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['users'].columns['department'].create()
    post_meta.tables['users'].columns['first_name'].create()
    post_meta.tables['users'].columns['last_name'].create()
    post_meta.tables['users'].columns['other_name'].create()
    post_meta.tables['users'].columns['role'].create()
    post_meta.tables['users'].columns['verified'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['users'].columns['department'].drop()
    post_meta.tables['users'].columns['first_name'].drop()
    post_meta.tables['users'].columns['last_name'].drop()
    post_meta.tables['users'].columns['other_name'].drop()
    post_meta.tables['users'].columns['role'].drop()
    post_meta.tables['users'].columns['verified'].drop()
