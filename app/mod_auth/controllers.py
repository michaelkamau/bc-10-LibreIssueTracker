
from flask import render_template, request, flash, redirect, url_for, Blueprint
from app.mod_auth.views import RegistrationForm

from app.models import User
from app import db

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

        return redirect(url_for('login'))

    return render_template('auth/register.html', form=form)

@mod_auth.route('/login', methods=['GET', 'POST'])
def login():
    pass

