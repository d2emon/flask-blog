from flask import Blueprint


blueprint = Blueprint('translate', __name__)


from . import routes
