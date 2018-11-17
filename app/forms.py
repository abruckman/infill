from flask_wtf import FlaskForm
from wtforms import SubmitField

class FileForm(FlaskForm):
        submit = SubmitField('Create Accounts')
