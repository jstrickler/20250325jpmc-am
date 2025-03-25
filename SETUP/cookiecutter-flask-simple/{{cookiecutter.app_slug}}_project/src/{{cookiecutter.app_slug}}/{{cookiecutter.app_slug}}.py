from flask import (
    Blueprint, g, render_template, request
)

from {{cookiecutter.app_slug}}.auth import login_required
from {{cookiecutter.app_slug}}.db import get_db

bp = Blueprint('{{cookiecutter.app_module}}', __name__)

@bp.route('/')
@login_required
def home():
    # db = get_db()  # not yet needed
    return render_template('{{cookiecutter.app_module}}/home.html', home_page=True)

@bp.route('/other')
@login_required
def other():
    return render_template('{{cookiecutter.app_module}}/other.html')