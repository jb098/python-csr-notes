"""
Flask routes. Some login code from the Flask-login docs.
https://flask-login.readthedocs.org/en/latest/

User loader code also from
https://realpython.com/blog/python/using-flask-login-for-user-management-with-flask/
"""
import time
from flask import Blueprint, redirect, url_for, render_template, flash, request
from flask_login import login_user, LoginManager, login_required, current_user, logout_user
from db import User, Note, Customer, add_record
from forms import LoginForm, CustomerForm, NotesForm, SearchForm


pages = Blueprint('pages', __name__, static_folder="static")

login_manager = LoginManager()

@login_manager.user_loader
def user_loader(user_id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve
    """
    return User.query.get(user_id)


@pages.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(
            email=request.form['email'],
            password=request.form['password']).first()
        if user is None:
            flash('Username or Password is invalid' , 'error')
            return redirect(url_for('.login'))
        login_user(user, remember=True)
        user.authenticated = True # login_user appears to be failing, workaround
        add_record(user)
        flash('Logged in successfully.')
        return redirect(url_for('.customer'))
    else:
        flash('Login failed')
    return render_template('login.html', form=form)


@pages.route('/')
def index():
    return redirect(url_for('.login'))


@pages.route('/customer', methods=['GET', 'POST'])
@login_required
def customer():
    if request.method == 'GET':
        form = SearchForm()
        return render_template('customer.html', form=form)
    elif request.method ==  'POST':
        return redirect(url_for('.notes', cocoon_id=request.form['search']))


@pages.route('/add_customer', methods=['GET', 'POST'])
@login_required
def add_customer():
    if request.method == 'GET':
        form = CustomerForm()
        return render_template('add_customer.html', form=form)
    elif request.method ==  'POST':
        customer = Customer(
            request.form['cocoon_ID'],
            request.form['title'],
            request.form['forename'],
            request.form['surname'])
        add_record(customer)
        redirect(url_for('.customer'))


@pages.route('/notes/<int:cocoon_id>', methods=['GET', 'POST'])
@login_required
def notes(cocoon_id):
    if request.method == 'GET':
        customer_notes = Note.query.filter_by(customer_id=cocoon_id)
        customer_details = Customer.query.filter_by(
            customer_id=cocoon_id).first()
        form = NotesForm()
        return render_template(
            'notes.html',
            form=form,
            notes=customer_notes,
            customer=customer_details)
    elif request.method == 'POST':
        note = Note(
            request.form['note'],
            current_user.email,
            cocoon_id,
            int(time.time()))
        add_record(note)
        return redirect(url_for('.notes', cocoon_id=request.form['search']))



@pages.route("/logout", methods=["GET"])
@login_required
def logout():
    """Logout the current user."""
    user = current_user
    user.authenticated = False
    add_record(user)
    logout_user()
    form = LoginForm()
    flash('Logged out successfully.')
    return render_template("login.html", form=form)


@pages.route('/register' , methods=['GET','POST'])
def register():
    if request.method == 'GET':
        form = LoginForm()
        return render_template('register.html', form=form)
    elif request.method == 'POST':
        user = User(
            request.form['email'],
            request.form['password'])
        add_record(user)
        flash('User successfully registered')
    return redirect(url_for('.login'))
