from flask import render_template, request, flash, redirect, Blueprint
from flask import session
from flask import url_for
from flask_login import login_required, current_user

from app import db
from app.mod_issues_tracker.views import NewIssueForm, AssignIssueForm
from app.models import Issue, User, Comment, AssignedIssue

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

    if current_user.is_admin():
        issues_list = db.session.query(Issue, User).filter(User.id == Issue.user).all()
    else:
        user_id = current_user.get_id()
        issues_list = db.session.query(Issue, User).filter(User.id == Issue.user, Issue.user == user_id)\
            .all()

    return render_template('issues/issues_list.html', issues_list=issues_list)


@mod_issue_tracker.route('/<int:issue_id>', methods=['GET', 'POST'])
@login_required
def get_issue_by_id(issue_id):
    form = AssignIssueForm(request.form)

    if request.method == 'POST':
        assign_user = form.users.data
        admin_comment = form.admin_comment.data

        # todo fix error not create new comments
        assigned_issue = AssignedIssue(user_id=assign_user, issue_id=issue_id)

        if admin_comment:
            comment = Comment(issue_id=issue_id, admin_comment=admin_comment)
            db.session.add(comment)

        db.session.add(assigned_issue)
        db.session.commit()

        flash("Assigned #" + str(issue_id) + " To " + session['username'])

        return redirect(url_for('issues.get_issues'))
    issue = db.session.query(Issue, User).filter(User.id == Issue.user).filter_by(id=issue_id).all()
    return render_template('issues/issue_details.html', issue=issue, form=form)
