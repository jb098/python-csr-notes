"""
Flask routes. Some login code from the Flask-login docs.
https://flask-login.readthedocs.org/en/latest/

User loader code also from
https://realpython.com/blog/python/using-flask-login-for-user-management-with-flask/
"""
from flask_wtf import LoginForm
from db import User


@login_manager.user_loader
def user_loader(user_id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve
    """
    return User.query.get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        login_user(user)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        if not next_is_valid(next):
            return flask.abort(400)

        return flask.redirect(next or flask.url_for('index'))
    return flask.render_template('login.html', form=form)


@app.route('/notes', methods=['GET', 'POST'])
@login_required
def notes():


@app.route("/logout", methods=["GET"])
@login_required
def logout():
    """Logout the current user."""
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return render_template("login.html")
