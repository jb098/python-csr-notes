"""
Flask routes. Some login code from the Flask-login docs.
https://flask-login.readthedocs.org/en/latest/

User loader code also from
https://realpython.com/blog/python/using-flask-login-for-user-management-with-flask/
"""
from flask import Blueprint, redirect, url_for, render_template
from flask_login import login_user, LoginManager, login_required
from db import User, Note
from forms import LoginForm

pages = Blueprint('pages', __name__, static_folder="static")

login_manager = LoginManager()

@login_manager.user_loader
def user_loader(user_id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve
    """
    return User.query.get(user_id)


@pages.route('/')
def index():
    return redirect(url_for('login'))


@pages.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_user(user)
        flask.flash('Logged in successfully.')
        return flask.redirect(flask.url_for('notes'))
    return render_template('login.html', form=form)


@pages.route('/notes', methods=['GET', 'POST'])
@login_required
def notes():
    if request.method == 'GET':
        notes = {}
        return render_template('notes.html', notes=notes)
    elif request.method == 'POST':
        pass



@pages.route("/logout", methods=["GET"])
@login_required
def logout():
    """Logout the current user."""
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    form = LoginForm()
    flask.flash('Logged out successfully.')
    return render_template("login.html", form=form)
