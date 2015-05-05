"""
Flask routes. Some login code from the Flask-login docs.
https://flask-login.readthedocs.org/en/latest/

User loader code also from
https://realpython.com/blog/python/using-flask-login-for-user-management-with-flask/
"""
from db import User

@login_manager.user_loader
def user_loader(user_id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve
    """
    return User.query.get(user_id)
