from flask import Response
from flask import render_template, request, flash, redirect, url_for, Blueprint

mod_index = Blueprint('index', __name__, url_prefix='/')


@mod_index.route('/', methods=['GET'])
def index():
    return Response(response=render_template('index/base.html'), status=200)
