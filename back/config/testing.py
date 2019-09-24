from .base import Config


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True
