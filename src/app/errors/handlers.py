from app import db
from app.api.errors import error_response as api_error_response
from flask import render_template, request
from . import blueprint


def wants_json_response():
    return request.accept_mimetypes['application/json'] >= request.accept_mimetypes['text/html']


@blueprint.app_errorhandler(404)
def error404(error):
    if wants_json_response():
        return api_error_response(404)
    return render_template('errors/404.html'), 404


@blueprint.app_errorhandler(500)
def error500(error):
    db.session.rollback()
    if wants_json_response():
        return api_error_response(500)
    return render_template('errors/500.html'), 500
