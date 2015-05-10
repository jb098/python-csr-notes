from flask_wtf import Form
from wtforms import TextField, PasswordField, validators

class LoginForm(Form):
    email = TextField('Email', [validators.Required()])
    password = PasswordField('Password', [validators.Required()])

class NotesForm(Form):
    note = TextField('Note')
