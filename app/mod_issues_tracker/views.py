from wtforms import Form, StringField, SelectField, TextAreaField
from wtforms import RadioField

from app.models import Department, User, IssueStatus


class NewIssueForm(Form):
    title = StringField(id="title")
    department = SelectField(id="department",
                             choices=Department().query.with_entities(Department.id, Department.name).all())
    priority = RadioField(id="priority", choices=[
        ("low", "Low"), ("medium", "Medium"), ("high", "High")
    ])
    description = TextAreaField(id="description")


class AssignIssueForm(Form):
    users = SelectField(id="assign_user", choices=User.query.with_entities(User.id, User.fullname).all())
    action_issue = SelectField(id="action_issue", choices=[(IssueStatus.CLOSED, "Close"),
                                                           (IssueStatus.IN_PROGRESS, "In Progress"),
                                                           (IssueStatus.OPEN, "Open")
                                                           ])
    admin_comment = TextAreaField(id="admin_comment")
