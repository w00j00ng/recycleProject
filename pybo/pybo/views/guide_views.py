from flask import Blueprint, render_template, session
from pybo.config import homedir
import json


bp = Blueprint('guide', __name__, url_prefix='/guide/')


@bp.route('/guide_all/')
def guide_all():
    return render_template('guide_all.html')


@bp.route('/by_class/<string:data>/', methods=['GET', 'POST'])
def guide(data):
    with open(homedir + '/static/guide/' + data + '.json', 'r', encoding="UTF-8") as f:
        guide_json = json.load(f)
    user_id = session.get('user_id')
    return render_template('guide.html', guide_json=guide_json,  user_id=user_id)
