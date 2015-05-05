"""
app file used to initialise server
"""
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager


def create_app():
    db = SQLAlchemy()
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
