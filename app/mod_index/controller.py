from flask import Response
from flask import render_template, app, request, flash, redirect, url_for, Blueprint
from flask_login import current_user

mod_index = Blueprint('index', __name__)


@mod_index.route('/', methods=['GET'])
def index():
    return Response(response=render_template('index/index.html'))
