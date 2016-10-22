from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
Comments = Table('Comments', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('issue_id', INTEGER),
    Column('comment', VARCHAR(length=250)),
)

Comments = Table('Comments', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('issue_id', Integer),
    Column('description', String(length=250)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['Comments'].columns['comment'].drop()
    post_meta.tables['Comments'].columns['description'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['Comments'].columns['comment'].create()
    post_meta.tables['Comments'].columns['description'].drop()
