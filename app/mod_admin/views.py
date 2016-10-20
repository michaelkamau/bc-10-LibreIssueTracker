from wtforms import Form, StringField, SelectField

from app import db
from app.models import User


class NewDepartmentForm(Form):
    department_name = StringField(id='department_name')
    users = SelectField(id='users',
                        choices=db.session.query(User.id, User.fullname).all()
                        )
