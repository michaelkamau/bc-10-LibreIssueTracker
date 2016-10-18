# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

from app.mod_auth.controllers import mod_auth as auth_module
from app.mod_issues_tracker.controllers import mod_issue_tracker as issue_tracker_module

app.register_blueprint(auth_module)
app.register_blueprint(issue_tracker_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
