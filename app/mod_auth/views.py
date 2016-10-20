from wtforms import Form, PasswordField, SelectField
from wtforms import StringField
from wtforms.validators import DataRequired, Email

from app.models import Department


class RegistrationForm(Form):
    username = StringField(id='username')
    email = StringField(id='email', validators=[DataRequired(), Email()])
    password = PasswordField(id='password')
    first_name = StringField(id='first_name')
    last_name = StringField(id='last_name')
    department = SelectField(id='department',
                             choices=Department().query.with_entities(Department.id, Department.name).all())


class LoginForm(Form):
    username = StringField(id="username")
    password = StringField(id="password")
