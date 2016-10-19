#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask_login import UserMixin

from app import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120), index=True)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    fullname = db.column_property(last_name + ", " + first_name)
    role = db.Column(db.Integer)
    verified = db.Column(db.Integer)
    department = db.Column(db.Integer, db.ForeignKey('departments.id'))

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

    def get_users(self):
        result = self.__class__.query.with_entities(
            self.__class__.id,
            self.__class__.fullname
        ).all()

        return list(result)

    def __repr__(self):
        return 'User %s email %s first %slast %s department %s ' % (self.username,
                                                                    self.email, self.first_name, self.last_name,
                                                                    self.department)


class Department(db.Model):
    __tablename__ = "departments"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120))
    admin_id = db.Column(db.Integer)

    def get_departments(self):
        result = self.__class__.query.with_entities(
            self.__class__.id,
            self.__class__.name
        ).all()
        return list(result)


class Issue(db.Model):
    __tablename__ = "issues"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120))
    description = db.Column(db.String(120))
    user = db.Column(db.Integer, db.ForeignKey('users.id'))
    priority = db.Column(db.Integer)
    status = db.Column(db.Integer)
    department = db.Column(db.Integer)
    created_at = db.Column(db.Integer)

    def __repr__(self):
        return 'Id: %s title: %s user: %s ' % (self.id, self.title, self.user)


class IssueStatus(object):
    NEW = 0
    IN_PROGRESS = 1
    OPEN = 2
    CLOSED = 3

    LOW = 0
    MEDIUM = 1
    HIGH = 2
