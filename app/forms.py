from wtforms import Form, BooleanField, StringField, PasswordField, validators, TextField, SelectField,SubmitField

class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    email = TextField("Email",[validators.Required("Please enter your email address."),
            validators.Email("Please enter your email address.")])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    language = SelectField('Languages', choices = [('cpp', 'C++'), 
      ('py', 'Python')])
    submit = SubmitField("SignUp")

