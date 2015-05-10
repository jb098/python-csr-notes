"""
Database controller for logins. User model code from
https://realpython.com/blog/python/using-flask-login-for-user-management-with-flask/
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Customer(db.Model):
    __tablename__ = 'customer'
    cocoon_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    notes = db.relationship('Note', backref='customer',
                                lazy='dynamic')


class Note(db.Model):
    """
    Model for a notes table
    """
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    note_text = db.Column(db.Text)
    user_email = db.Column(db.String, db.ForeignKey('user.email'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.cocoon_id'))
    timestamp = db.Column(db.DateTime)


class User(db.Model):
    """An admin user capable of viewing reports.

    :param str email: email address of user
    :param str password: encrypted password for the user

    """
    __tablename__ = 'user'

    email = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)
    authenticated = db.Column(db.Boolean, default=False)
    notes = db.relationship('Note', backref='user',
                                lazy='dynamic')

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

def add_record(record):
    db.session.add(record)
    db.session.commit()
