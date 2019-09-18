def handler_factory(f):
    def wrapped(
        config,
        formatter=None,
        level=None,
    ):
        handler = f(config)
        if formatter:
            handler.setFormatter(formatter)
        if level:
            handler.setLevel(level)
        return handler
    return wrapped
