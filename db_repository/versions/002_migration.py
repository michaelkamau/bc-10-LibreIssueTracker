from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
AssignedIssues = Table('AssignedIssues', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('user', INTEGER),
    Column('issue', INTEGER),
)

AssignedIssues = Table('AssignedIssues', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('user_id', Integer),
    Column('issue_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['AssignedIssues'].columns['issue'].drop()
    pre_meta.tables['AssignedIssues'].columns['user'].drop()
    post_meta.tables['AssignedIssues'].columns['issue_id'].create()
    post_meta.tables['AssignedIssues'].columns['user_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['AssignedIssues'].columns['issue'].create()
    pre_meta.tables['AssignedIssues'].columns['user'].create()
    post_meta.tables['AssignedIssues'].columns['issue_id'].drop()
    post_meta.tables['AssignedIssues'].columns['user_id'].drop()
