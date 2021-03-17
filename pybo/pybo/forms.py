from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired


class UploadImageForm(FlaskForm):
    inputFile = FileField('사진', validators=[FileRequired()])
