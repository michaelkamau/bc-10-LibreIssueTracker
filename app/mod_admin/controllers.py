from flask import Blueprint
from flask import flash
from flask import render_template
from flask import request
from flask_login import login_required

from app import db
from app.mod_admin.views import NewDepartmentForm
from app.mod_auth.controllers import requires_roles
from app.models import Department, User, Role

mod_admin = Blueprint('admin', __name__, url_prefix='/admin')


@mod_admin.route('/departments', methods=['GET', 'POST'])
@login_required
@requires_roles(Role.admin)
def manage_departments():

    form = NewDepartmentForm(request.form)

    if request.method == 'POST':
        name = form.department_name.data
        admin_id = form.users.data

        department = Department(admin_id=admin_id, name=name)

        db.session.add(department)
        db.session.commit()

        flash("Created New Department Succesfully", category='info')

    departments = db.session.query(Department.id, Department.name, User.fullname) \
        .outerjoin(User, Department.admin_id == User.id).all()

    return render_template('admin/departments.html', departments=departments, form=form)

