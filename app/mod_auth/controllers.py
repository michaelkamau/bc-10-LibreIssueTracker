from flask import render_template, request, flash, redirect, url_for, Blueprint

from app import db
from app.mod_auth.views import RegistrationForm
from app.mod_auth.views import LoginForm
from app.models import User

mod_auth = Blueprint('auth', __name__, url_prefix='/auth')


@mod_auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST':
        user = User(
            username=form.username.data,
            password=form.password.data,
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            other_name=form.other_name.data,
            department=form.department.data
        )
        db.session.add(user)
        db.session.commit()

        flash('Thanks for registering')

        return redirect(url_for('auth/login'))

    return render_template('auth/register.html', form=form)


@mod_auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if request.method == 'POST':
        username = form.username.data
        password = form.password.data

        q = db.session.query(User).filter(User.username == username, User.password == password).exists()
        if db.session.query(q).scalar():
            # todo add session
            return "logged in, start session"
        else:
            return "Unknown User/password combination"

    return render_template('auth/login.html', form=form)
