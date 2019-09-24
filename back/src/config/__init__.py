import os
from .base import Config as BaseConfig
from .development import DevelopmentConfig
from .production import ProductionConfig
from .testing import TestingConfig


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
}


FLASK_ENV = os.environ.get('FLASK_ENV') or 'production'
Config = config.get(FLASK_ENV, ProductionConfig)
