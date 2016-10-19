# Import flask and template operators
from flask import Flask

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app.mod_auth.controllers import mod_auth as auth_module
from app.mod_issues_tracker.controllers import mod_issue_tracker as issue_tracker_module
from app.mod_index.controller import mod_index as index_module

app.register_blueprint(auth_module)
app.register_blueprint(issue_tracker_module)
app.register_blueprint(index_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
