class Config(object):
    SQLALCHEMY_DATABASE_URI = "sqlite:///csr.db"
    DEBUG = True
    SECRET_KEY = "CHANGEME"
    WTF_CSRF_ENABLED = False
