from flask import Blueprint, render_template


bp = Blueprint('classifier', __name__, url_prefix='/classifier/')


@bp.route('/')
def index():
    return render_template('classifier.html')
