from .base import Config


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True
    SERVER_NAME = '127.0.0.1'
