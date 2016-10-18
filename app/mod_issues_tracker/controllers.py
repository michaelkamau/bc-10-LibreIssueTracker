
from flask import render_template, request, flash, redirect, url_for, Blueprint

from app import db
from app.mod_issues_tracker.views import NewIssueForm
from app.models import Issue

mod_issue_tracker = Blueprint('issue', __name__, url_prefix='/issue')


@mod_issue_tracker.route('/new', methods=['GET', 'POST'])
def register():
    form = NewIssueForm(request.form)
    if request.method == 'POST':
        title = form.title.data
        department = form.department.data
        priority = form.priority.data
        description = form.description.data

        issue = Issue(
            title=title,
            department=department,
            priority=priority,
            description=description,
            user=2,
            status=0
        )

        print "State %s", db.session.add(issue)
        db.session.commit()

        return  "issue submitted"

    return render_template('issue/create_new.html', form=form)

