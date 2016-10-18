#!/usr/bin/python
# -*- coding: utf-8 -*-
from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(120), index=True)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    other_name = db.Column(db.String(120))
    role = db.Column(db.Integer)
    verified = db.Column(db.Integer)
    department = db.Column(db.Integer, db.ForeignKey('departments.id'))

    def __repr__(self):
        return 'User %s email %s first %slast %s department %s ' % (self.username,
                                                                    self.email, self.first_name, self.last_name,
                                                                    self.department)


class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120))
    admin_id = db.Column(db.Integer)

    def get_departments(self):
        result = self.__class__.query.with_entities(
            self.__class__.id,
            self.__class__.name
        )
        return list(result)


class Issue(db.Model):
    __tablename__ = "issues"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120))
    description = db.Column(db.String(120))
    user = db.Column(db.Integer, db.ForeignKey('users.id'))
    priority = db.Column(db.Integer)
    status = db.Column(db.Integer)
    department=db.Column(db.Integer)

    def __repr__(self):
        return 'Id: %s title: %s user: %s ' % (self.id, self.title, self.user)

