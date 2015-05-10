from flask_wtf import Form
from db import db
from wtforms import TextField, PasswordField, validators

class LoginForm(Form):
    email = TextField('Email', [validators.Required()])
    password = PasswordField('Password', [validators.Required()])

class NotesForm(Form):
    note = TextField('Note')

class SearchForm(Form):
    search = TextField('Cocoon ID')

class CustomerForm(Form):
    cocoon_ID = TextField('Cocoon ID', [validators.Required()])
    title = TextField('Title', [validators.Required()])
    forename = TextField('Forename', [validators.Required()])
    surname = TextField('Surname', [validators.Required()])
