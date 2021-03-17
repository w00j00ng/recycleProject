from flask import Blueprint, render_template, request
from pybo.classify import clf
from pybo.config import homedir
from pybo.forms import UploadImageForm
import os

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    form = UploadImageForm()
    return render_template('index.html', form=form)


@bp.route('/guide/', methods=['GET', 'POST'])
def classifier():
    inputImage = request.files['file']
    fdir = homedir + "/static/" + inputImage.filename
    inputImage.save(fdir)
    data = clf(fdir)
    os.remove(fdir)

    return render_template('guide_' + data + '.html', data=data)
