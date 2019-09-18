from logging.handlers import RotatingFileHandler
from .handler import handler_factory


@handler_factory
def file_handler(config):
    return RotatingFileHandler(
        config['LOG_FILENAME'],
        maxBytes=config['LOG_FILE_MAX_BYTES'],
        backupCount=config['LOG_FILE_BACKUP_COUNT'],
    )
