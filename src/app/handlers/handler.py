import logging


def handler_factory(f):
    def wrapped(
        app,
        formatter=None,
        level=None,
    ):
        handler = f(app.config)
        if formatter:
            handler.setFormatter(formatter)
        handler.setLevel(level or app.logger.level)
        app.logger.addHandler(handler)
    return wrapped
