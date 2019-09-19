from flask import render_template
from . import blueprint


@blueprint.app_errorhandler(404)
def error404(error):
    return render_template('errors/404.html'), 404


@blueprint.app_errorhandler(500)
def error500(error):
    return render_template('errors/500.html'), 500
