from .file_handler import file_handler
from .mail_handler import mail_handler


handlers = {
    'FILE': file_handler,
    'MAIL': mail_handler,
}


def register_handlers(app):
    level = app.config.get('LOG_LEVEL')
    if level:
        app.logger.setLevel(level)

    for key, config in app.config.get('LOG_HANDLERS', {}).items():
        if config:
            try:
                handlers[key](app, **config)
            except Exception as e:
                app.logger.error(e)

    app.logger.debug(app.config)
