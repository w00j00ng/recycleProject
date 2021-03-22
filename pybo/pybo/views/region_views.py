from flask import Blueprint, render_template, request, session
from pybo.forms import RegionForm
from pybo.schedule import regionList, guideStr


bp = Blueprint('region', __name__, url_prefix='/region/')


@bp.route('/', methods=['GET', 'POST'])
def index():
    form = RegionForm
    if request.method == 'POST' and request.form['keyword']:
        address = request.form['keyword']
        if address not in regionList:
            guide_str = ["지역구를 다시 입력해주세요", ""]
            return render_template('region.html', form=form, address=address, guide_str=guide_str, notvalid=True)
        guide_str = guideStr(address)
        return render_template('region.html', form=form, address=address, guide_str=guide_str, valid=True)

    address = session.get('address')
    if address is None or address not in regionList:
        render_template('region.html', form=form)
        return render_template('region.html', form=form)
    guide_str = guideStr(address)
    return render_template('region.html', form=form, address=address, guide_str=guide_str, valid=True)