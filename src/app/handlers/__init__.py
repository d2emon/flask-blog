from app import app
from .file_handler import file_handler
from .mail_handler import mail_handler


handlers = {
    'FILE': file_handler,
    'MAIL': mail_handler,
}


for key, config in app.config.get('LOG_HANDLERS', {}).items():
    if config:
        app.logger.addHandler(handlers[key](app.config, **config))


level = app.config.get('LOG_LEVEL')
if level:
    app.logger.setLevel(level)


app.logger.info('Blog startup')
app.logger.debug(app.config)
