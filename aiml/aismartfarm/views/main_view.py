from flask import Blueprint, url_for
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, render_template
from werkzeug.utils import redirect
#from services.pipeline import run_pipeline

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return render_template('main/result.html')

@bp.route('/main')
def hello_flask():
    return "hello, flask"
