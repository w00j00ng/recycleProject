from flask import Blueprint, render_template, redirect, url_for
from pybo.classify import clf
from pybo.config import homedir
import os
from pybo.forms import PhotoForm, GameForm
from werkzeug.utils import secure_filename
import json


bp = Blueprint('game', __name__, url_prefix='/game/')


@bp.route('/', methods=['GET', 'POST'])
def index():
    form = GameForm()
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

        answer = form.answer.data

        with open(homedir + '/static/guide/' + data + '.json', 'r', encoding="UTF-8") as f:
            guide_json = json.load(f)

            if (data == 'battery' and answer == '배터리') \
                or (data == 'cardboard' and answer == '상자류') \
                or (data == 'glass' and answer == '유리') \
                or (data == 'metal' and answer == '금속') \
                or (data == 'paper' and answer == '종이') \
                or (data == 'plastic' and answer == '플라스틱') \
                or (data == 'trash' and answer == '일반쓰레기'):
                return render_template('game_result.html', data=data, correct=True, guide_json=guide_json)
            else:
                return render_template('game_result.html', data=data, correct=False, guide_json=guide_json)
    return render_template('game.html', form=form)


@bp.route('/result/', methods=['GET', 'POST'])
def result(data):
    print("==============================")
    print(data)
    print("==============================")
    return "success"
