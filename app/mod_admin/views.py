from wtforms import Form, StringField, SelectField
from wtforms.validators import DataRequired

from app import db
from app.models import User


class NewDepartmentForm(Form):
    department_name = StringField(id='department_name',  validators=[DataRequired()])
    users = SelectField(id='users',  validators=[DataRequired()],
                        choices=db.session.query(User.id, User.fullname).all()
                        )
