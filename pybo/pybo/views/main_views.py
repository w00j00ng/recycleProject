from flask import Blueprint, render_template, redirect, url_for, request
from pybo.classify import myFunc

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/guide/', methods=['GET', 'POST'])
def classifier():
    inputImage = request.files['file']
    inputImage.save("c:/users/yong/desktop/"+inputImage.filename)
    return render_template('guide.html', data=inputImage)
