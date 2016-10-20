from wtforms import Form, PasswordField, StringField, SelectField

from app.models import Department


class RegistrationForm(Form):
    username = StringField(id='username')
    email = StringField(id='email')
    password = PasswordField(id='password')
    confirm_password = PasswordField(id='confirm_password')
    first_name = StringField(id='first_name')
    last_name = StringField(id='last_name')
    department = SelectField(id='department',
                             choices=Department().query.with_entities(Department.id, Department.name).all())


class LoginForm(Form):
    username = StringField(id="username")
    password = StringField(id="password")
