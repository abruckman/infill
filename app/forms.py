from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField

class FileForm(FlaskForm):
    csv_file = FileField('csv', validators=[
        FileRequired()
    ])
    submit = SubmitField('Create Accounts')
