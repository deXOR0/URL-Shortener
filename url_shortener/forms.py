from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class URL(FlaskForm):
    url = StringField('URL', validators=[DataRequired()])
    short_url = StringField('Short URL')
    submit = SubmitField('Submit')