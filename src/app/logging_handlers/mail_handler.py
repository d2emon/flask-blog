from logging.handlers import SMTPHandler
from .handler import handler_factory


@handler_factory
def mail_handler(config):
    if config.get('MAIL_USERNAME') or config.get('MAIL_PASSWORD'):
        credentials = (config.get('MAIL_USERNAME'), config.get('MAIL_PASSWORD'))
    else:
        credentials = None

    return SMTPHandler(
        mailhost=(config['MAIL_SERVER'], config['MAIL_PORT']),
        fromaddr="no-reply@{}".format(config['MAIL_SERVER']),
        toaddrs=config['ADMINS'],
        subject=config.get('LOG_MAIL_SUBJECT'),
        credentials=credentials,
        secure=config.get('MAIL_USE_TLS') and (),
    )
