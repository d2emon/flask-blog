from flask import Blueprint


blueprint = Blueprint('blog_blueprint', __name__)


from . import routes
