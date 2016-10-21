from wtforms import Form, PasswordField, SelectField
from wtforms import StringField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap

from app import app

Bootstrap(app)

from app.models import Department


class RegistrationForm(Form):
    username = StringField(id='username', validators=[DataRequired()])
    email = StringField(id='email', validators=[DataRequired(), Email()])
    password = PasswordField(id='password', validators=[DataRequired()])
    first_name = StringField(id='first_name', validators=[DataRequired()])
    last_name = StringField(id='last_name', validators=[DataRequired()])
    department = SelectField(id='department',
                             choices=Department().query.with_entities(Department.id, Department.name).all())


class LoginForm(Form):
    username = StringField(id="username", validators=[DataRequired()])
    password = StringField(id="password", validators=[DataRequired()])
    hidden_tag = StringField()

