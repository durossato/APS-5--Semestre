from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

class ExtrairForm(FlaskForm):
    link = SelectField("link", choices=[('https://www.tecmundo.com.br/novidades'),('https://www.megacurioso.com.br/novidades/')],)

class News(FlaskForm):
    link = StringField()