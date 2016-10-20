
from flask import render_template, request, flash, redirect, url_for, Blueprint
from flask import session
from flask_login import login_required

from app import db
from app.mod_issues_tracker.views import NewIssueForm, AssignIssueForm
from app.models import Issue, User

mod_issue_tracker = Blueprint('issues', __name__, url_prefix='/issues')


@mod_issue_tracker.route('/new', methods=['GET', 'POST'])
@login_required
def add_new_issue():
    form = NewIssueForm(request.form)
    if request.method == 'POST':
        title = form.title.data
        department = form.department.data
        priority = form.priority.data
        description = form.description.data
        user_id = session['user_id']

        issue = Issue(
            title=title,
            department=department,
            priority=priority,
            description=description,
            user=user_id,
            status=0
        )

        print description

        db.session.add(issue)
        db.session.commit()

        flash("Issue Submitted Successfully", category='info')

        return redirect("/issues")

    return render_template('issues/create_new.html', form=form)


@mod_issue_tracker.route('/', methods=['GET'])
@login_required
def get_issues():

    if request.method == 'GET':
        issues_list = db.session.query(Issue, User).filter(User.id == Issue.user).all()

        return render_template('issues/issues_list.html', issues_list=issues_list)


@mod_issue_tracker.route('/<int:issue_id>', methods=['GET', 'POST'])
def get_issue_by_id(issue_id):
    form = AssignIssueForm()
    issue = None
    if request.method == 'POST':
        assign_user = form.users.data
        commment = form.data




    if issue_id:
        issue = db.session.query(Issue, User).filter(User.id == Issue.user).filter_by(id=issue_id).all()
    return render_template('issues/issue_details.html', issue=issue, form=form)

