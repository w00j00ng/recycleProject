from flask import Blueprint, render_template, request, redirect, url_for, session, g
from pybo.classify import clf
from pybo.config import homedir
import os
from pybo.forms import PhotoForm, RegionForm
from werkzeug.utils import secure_filename
import json
from pybo.schedule import regionList, guideStr
from pybo.models import User


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


@bp.route('/guide_all/')
def guide_all():
    return render_template('guide_all.html')


@bp.route('/guide/<string:data>', methods=['GET', 'POST'])
def guide(data):
    with open(homedir + '/static/guide/' + data + '.json', 'r', encoding="UTF-8") as f:
        guide_json = json.load(f)
    user_id = session.get('user_id')
    return render_template('guide.html', guide_json=guide_json,  user_id=user_id)


@bp.route('/region/', methods=['GET', 'POST'])
def region():
    form = RegionForm
    if request.method == 'POST' and request.form['keyword']:
        keyword = request.form['keyword']
        if keyword not in regionList:
            guide_str = ["지역구를 다시 입력해주세요", ""]
            return render_template('region.html', form=form, keyword=keyword, guide_str=guide_str, notvalid=True)
        guide_str = guideStr(keyword)
        return render_template('region.html', form=form, keyword=keyword, guide_str=guide_str, valid=True)

    address = session.get('address')
    if address is None or address not in regionList:
        render_template('region.html', form=form)
        return render_template('region.html', form=form)
    guide_str = guideStr(address)
    return render_template('region.html', form=form, address=address, guide_str=guide_str, valid=True)


@bp.route('/about/')
def about():
    return render_template('about.html')
