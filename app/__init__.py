# Import flask and template operators
from flask import Flask

# Import SQLAlchemy
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config')
db = SQLAlchemy(app)

from app.mod_auth.controllers import mod_auth
from app.mod_issues_tracker.controllers import mod_issue_tracker
from app.mod_index.controller import mod_index
from app.mod_admin.controllers import mod_admin

app.register_blueprint(mod_auth)
app.register_blueprint(mod_issue_tracker)
app.register_blueprint(mod_index)
app.register_blueprint(mod_admin)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
