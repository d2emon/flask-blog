import logging
import os
from .base import Config


class ProductionConfig(Config):
    LOG_HANDLERS = {
        'FILE': {
            'level': logging.INFO,
        },
        'MAIL': {
            'level': logging.ERROR,
        },
    }
