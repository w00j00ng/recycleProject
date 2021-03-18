from flask import Blueprint, render_template, request, redirect, url_for
from pybo.classify import clf
from pybo.config import homedir
import os
from pybo.forms import PhotoForm
from werkzeug.utils import secure_filename
import json


bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/', methods=['GET', 'POST'])
def index():
    form = PhotoForm()
    if form.validate_on_submit():
        f = form.photo.data
        filename = secure_filename(f.filename)
        extension = os.path.splitext(filename)[1]
        if extension.lower() not in ('.jpg', '.jpeg', '.png'):
            return redirect(url_for('main.index'))
        fdir = homedir + '/static/' + filename
        f.save(fdir)
        data = clf(fdir)
        os.remove(fdir)
        return redirect(url_for('main.guide', data=data))
    return render_template('index.html', form=form)


@bp.route('/guide/<string:data>', methods=['GET', 'POST'])
def guide(data):
    with open(homedir + '/static/guide/' + data + '.json', 'r', encoding="UTF-8") as f:
        guide_json = json.load(f)
    return render_template('guide.html', data=guide_json)

