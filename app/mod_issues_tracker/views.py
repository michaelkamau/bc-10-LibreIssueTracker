from wtforms import Form, StringField, SelectField, TextAreaField
from wtforms import RadioField

from app.models import Department, User


class NewIssueForm(Form):
    title = StringField(id="title")
    department = SelectField(id="department", choices=Department().get_departments())
    priority = RadioField(id="priority", choices=[
        ("low", "Low"), ("medium", "Medium"), ("high", "High")
    ])
    description = TextAreaField(id="description")


class AssignIssueForm(Form):
    users = SelectField(label="User", choices=User().get_users())
    comment = TextAreaField(label="comments")
