from flask import Blueprint, render_template, request


bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print("request: ", request.form)

        return render_template('classifier.html')

    return render_template('index.html')
