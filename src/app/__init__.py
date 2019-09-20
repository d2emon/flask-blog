from config import Config
from elasticsearch import Elasticsearch
from flask import Flask, current_app, request
from flask_babel import Babel, lazy_gettext as _l
from flask_bootstrap import Bootstrap
from flask_cors import CORS
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from .logging_handlers import register_handlers


# Modules
babel = Babel()
bootstrap = Bootstrap()
# cache = Cache(app)
# toolbar = DebugToolbarExtension(app)
cors = CORS()
login = LoginManager()
mail = Mail()
# manager = Manager(app)
migrate = Migrate()
moment = Moment()
db = SQLAlchemy()
# # Session(app)


# Config modules
login.login_view = 'auth.login'
login.login_message = _l('Please log in to access this page.')

# db.create_all()


# Instantiate the app
def create_app(config_class=Config):
    app = Flask(__name__)
    # app = Flask(__name__, instance_relative_config=True)

    # Loading config
    app.config.from_object(config_class)
    # app.static_folder = app.config.get('STATIC_FOLDER', 'static')
    # app.template_folder = app.config.get('TEMPLATE_FOLDER', 'templates')

    babel.init_app(app)
    bootstrap.init_app(app)
    cors.init_app(app)
    db.init_app(app)
    login.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)
    moment.init_app(app)

    # Elastic search
    app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) if app.config['ELASTICSEARCH_URL'] else None

    # Register blueprints
    from .errors import blueprint as errors_blueprint
    app.register_blueprint(errors_blueprint)

    from .auth import blueprint as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .main import blueprint as main_blueprint
    app.register_blueprint(main_blueprint)

    from .translate import blueprint as translate_blueprint
    app.register_blueprint(translate_blueprint, url_prefix='/translate')

    # # from .admin import admin as admin_blueprint
    # # app.register_blueprint(admin_blueprint, url_prefix='/admin')

    register_handlers(app)

    return app


# Models
# # from execom import models
# from blog import models


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(current_app.config['LANGUAGES'])


# All
from app import models
