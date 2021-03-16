from flask import Blueprint, render_template, redirect, url_for, request


bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/guide/', methods=['GET', 'POST'])
def classifier():
    return render_template('guide.html')
