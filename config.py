import os

WTF_CSRF_ENABLED = True
SECRET_KEY = 'qwertyuiop[]oiuytrs'
CSRF_SESSION_KEY = "sdfyhnmvcfuioijhgcdtyuioiyf"

DEBUG = True

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

DATABASE_CONNECT_OPTIONS = {}
THREADS_PER_PAGE = 2
CSRF_ENABLED = True
