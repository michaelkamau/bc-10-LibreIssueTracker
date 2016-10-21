#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask_login import UserMixin

from app import db


class Department(db.Model):
    __tablename__ = "Departments"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120))
    admin_id = db.Column(db.Integer)


class User(db.Model, UserMixin):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120), index=True)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    fullname = db.column_property(last_name + ", " + first_name)
    role = db.Column(db.Integer, default=0)
    verified = db.Column(db.Integer)
    department = db.Column(db.Integer, db.ForeignKey(Department.id))

    def __init__(self, username=None, email=None, password=None, first_name=None,
                 last_name=None, department=None, role=0, verified=0
                 ):
        self.username = username
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.verified = verified
        self.department = department

    def is_admin(self):
        return self.role == 1

    def __repr__(self):
        return 'User %s email %s first %slast %s department %s ' % (self.username,
                                                                    self.email, self.first_name, self.last_name,
                                                                    self.department)


class Issue(db.Model):
    __tablename__ = "Issues"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120))
    description = db.Column(db.String(250))
    user = db.Column(db.Integer, db.ForeignKey(User.id))
    priority = db.Column(db.Integer, default="low")
    status = db.Column(db.Integer, default="0")
    department = db.Column(db.Integer)
    created_at = db.Column(db.Integer)

    def __repr__(self):
        return 'Id: %s title: %s user: %s ' % (self.id, self.title, self.user)


class AssignedIssue(db.Model):
    __tablename__ = "AssignedIssues"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    issue_id = db.Column(db.Integer, db.ForeignKey(Issue.id))

    def __repr__(self):
        return "Issue: %s User: %s " % (self.issue_id, self.user_id)


class Comment(db.Model):
    __tablename__ = "Comments"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    issue_id = db.Column(db.Integer, db.ForeignKey(Issue.id), index=True)
    admin_comment = description = db.Column(db.String(250))

    def __repr__(self):
        return "Issue_id: %s Comment_id: %s " % (self.issue_id, self.admin_comment)


class Role(object):
    admin = 1
    user = 0


class IssueStatus(object):
    OPEN = 0
    IN_PROGRESS = 1
    CLOSED = 2

    LOW = 0
    MEDIUM = 1
    HIGH = 2


