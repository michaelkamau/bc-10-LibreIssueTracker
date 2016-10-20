from flask import render_template, request, flash, redirect, url_for, Blueprint
from flask import session
from flask_login import login_user, logout_user, LoginManager, current_user

from app import db, app
from app.mod_auth.views import LoginForm
from app.mod_auth.views import RegistrationForm
from app.models import User

mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"


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
            department=form.department.data
        )
        db.session.add(user)
        db.session.commit()

        flash('Thanks for registering')

        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form)


@mod_auth.route('/logout', methods=['GET'])
def logout():
    if logout_user():
        flash("Successfully Logged out")
        return redirect(url_for("auth.login"))
    else:
        flash("problem logging out")
        return "done"


@mod_auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if request.method == 'POST':
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username, password=password).first()

        if user is not None:
            login_user(user, True)
            session['user_id'] = user.id
            session['username'] = user.username

            flash("Logged in")

            return redirect(url_for("index.index"))
        print request.args.get('next', 19, type=int)

    return render_template('auth/login.html', form=form)


def get_current_user_role():
    return current_user.is_admin()


def error_response():
    return "You've got no permission to access this page.", 403


def requires_roles(*roles):
    def wrapper(f):
        from functools import wraps

        @wraps(f)
        def wrapped(*args, **kwargs):
            if get_current_user_role() not in roles:
                return error_response()
            return f(*args, **kwargs)

        return wrapped

    return wrapper


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


