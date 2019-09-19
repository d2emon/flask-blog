from config import Config
from flask import Flask, request
from flask_babel import Babel, lazy_gettext as _l
from flask_bootstrap import Bootstrap
from flask_cors import CORS
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy


# Instantiate the app
app = Flask(__name__)
# app = Flask(__name__, instance_relative_config=True)

# Loading config
app.config.from_object(Config)
# app.config.from_pyfile('config.py')
# app.static_folder = app.config.get('STATIC_FOLDER', 'static')
# app.template_folder = app.config.get('TEMPLATE_FOLDER', 'templates')


# Modules
babel = Babel(app)
bootstrap = Bootstrap(app)
# cache = Cache(app)
# toolbar = DebugToolbarExtension(app)
CORS(app)
login = LoginManager(app)
mail = Mail(app)
# manager = Manager(app)
moment = Moment(app)
db = SQLAlchemy(app)
# # Session(app)
migrate = Migrate(app, db)


# Config modules
login.login_view = 'auth.login'
login.login_message = _l('Please log in to access this page.')

# db.create_all()


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# Models
# # from execom import models
# from blog import models


# Blueprints
from .errors import blueprint as errors_blueprint
app.register_blueprint(errors_blueprint)

from .auth import blueprint as auth_blueprint
app.register_blueprint(auth_blueprint, url_prefix='/auth')

# # from .admin import admin as admin_blueprint
# # app.register_blueprint(admin_blueprint, url_prefix='/admin')

# # from .home import home as home_blueprint
# # app.register_blueprint(home_blueprint)


# Views
# from app.views import *
# from blog.views import *


# All
from app import cli, handlers, routes, models
