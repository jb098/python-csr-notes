"""
app file used to initialise server
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from routes import pages

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(pages)
    db = SQLAlchemy()
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8080)
