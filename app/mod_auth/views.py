from wtforms import Form, PasswordField, StringField, SelectField

from app.models import Department


class RegistrationForm(Form):
    username = StringField('username')
    email = StringField("email")
    password = PasswordField('password')
    confirm_password = PasswordField('confirm_password')
    first_name = StringField("first_name")
    last_name = StringField("last_name")
    other_name = StringField("other_name")
    department = SelectField(choices=Department().get_departments())
