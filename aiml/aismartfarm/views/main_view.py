from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/main')
def hello_flask():
    return "hello, flask"

@bp.route('/')
def flask():
    return "flask index"
