from wtforms import Form, PasswordField, validators, TextField, SelectField, SubmitField


class RegistrationForm(Form):
    username = TextField('username', [validators.Length(min=4, max=25)])
    email = TextField("email", [validators.Required("Please enter your email address."),
                                validators.Email("Please enter your email address.")])
    password = PasswordField('password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('confirm password')
    language = SelectField('Languages', choices=[('cpp', 'C++'),
                                                 ('py', 'Python')])
