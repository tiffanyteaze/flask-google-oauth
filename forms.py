from flask_wtf import FlaskForm as Form
from wtforms import TextField, TextAreaField, SubmitField

from models import User

class UserForm(Form):
    username = TextField("Username")
    email = TextField("Email")
    first_name = TextField("First Name")
    last_name = TextField("Last Name")
    skin_type = TextField("Skin Type")
    submit = SubmitField('Edit User')