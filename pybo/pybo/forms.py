from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField
from werkzeug.utils import secure_filename
from wtforms.validators import DataRequired

class PhotoForm(FlaskForm):
    photo = FileField(validators=[FileRequired()])


class RegionForm(FlaskForm):
    region = StringField('name', validators=[DataRequired()])
