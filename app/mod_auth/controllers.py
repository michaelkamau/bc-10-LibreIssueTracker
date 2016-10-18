
from flask import render_template, request, flash, redirect, url_for, Blueprint
from app.mod_auth.forms import RegistrationForm

from app.mod_auth.models import User
from app import db

mod_auth = Blueprint('auth', __name__, url_prefix='/auth')


@mod_auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('auth/register.html', form=form)
