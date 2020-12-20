from flask_wtf import FlaskForm
from wtforms import StringField, TextField, BooleanField, IntegerField
from wtforms.validators import DataRequired

class DiscForm(FlaskForm):
    artist = StringField('artist', validators=[DataRequired()])
    title = StringField('title', validators=[DataRequired()])
    genre = StringField('genre', validators=[DataRequired()])
    year = IntegerField('year', validators=[DataRequired()])
    description = TextField('description', validators=[DataRequired()])
    rented = BooleanField('recommend', validators=[])

class ArtistForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    about = StringField('about', validators=[])