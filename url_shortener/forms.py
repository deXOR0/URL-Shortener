from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class URL(FlaskForm):
    url = StringField('URL', validators=[DataRequired()])
    short_url = StringField('Short URL')
    password = PasswordField('Password')
    submit = SubmitField('Submit')

class URL_Verification(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')