from flask import Blueprint, render_template, request
from pybo.classify import clf
from pybo.config import homedir
import os

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/guide/', methods=['GET', 'POST'])
def classifier():
    inputImage = request.files['file']
    fdir = homedir + "/static/" + inputImage.filename
    inputImage.save(fdir)
    data = clf(fdir)
    os.remove(fdir)

    return render_template('guide_' + data + '.html', data=data)
