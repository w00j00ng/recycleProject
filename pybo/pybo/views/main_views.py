from flask import Blueprint, render_template, request
from pybo.classify import clf
from pybo.config import homedir
import os
from pybo.forms import PhotoForm
from werkzeug.utils import secure_filename


bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/', methods=['GET', 'POST'])
def index():
    form = PhotoForm()
    if form.validate_on_submit():
        f = form.photo.data
        filename = secure_filename(f.filename)
        fdir = homedir + filename
        f.save(fdir)
        data = clf(fdir)
        return render_template('guide_' + data + '.html', data=data)
    return render_template('index.html', form=form)


@bp.route('/guide/', methods=['GET', 'POST'])
def classifier():
    inputImage = request.files['file']
    fdir = homedir + "/static/" + inputImage.filename
    inputImage.save(fdir)
    data = clf(fdir)
    os.remove(fdir)

    return render_template('guide_' + data + '.html', data=data)


