from flask import Blueprint
from flask import render_template
from flask_login import login_required

from app import db
from app.mod_auth.controllers import requires_roles
from app.models import Department, User, Role

mod_admin = Blueprint('admin', __name__, url_prefix='/admin')


@mod_admin.route('/departments', methods=['GET'])
@login_required
@requires_roles(Role.admin)
def manage_departments():

    departments_admin = Department.query.all()

    return render_template('admin/departments.html', dep_admin=departments_admin)

