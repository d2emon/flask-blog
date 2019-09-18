from config import Config
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_cors import CORS
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Instantiate the app
app = Flask(__name__)
# app = Flask(__name__, instance_relative_config=True)

# Loading config
app.config.from_object(Config)
# app.config.from_pyfile('config.py')
# app.static_folder = app.config.get('STATIC_FOLDER', 'static')
# app.template_folder = app.config.get('TEMPLATE_FOLDER', 'templates')

# log_config = app.config.get("LOG", dict())
# app.logger.addHandler(create_logger(log_config))


# Modules
bootstrap = Bootstrap(app)

# cache = Cache(app)

# toolbar = DebugToolbarExtension(app)

CORS(app)

login = LoginManager(app)
login.login_view = 'login'
login.login_message = "Пожалуйста, войдите, чтобы открыть эту страницу."

mail = Mail(app)

# manager = Manager(app)

db = SQLAlchemy(app)
# db.create_all()

migrate = Migrate(app, db)

# # Session(app)


# Models
# # from execom import models
# from blog import models


# Blueprints
# # from .admin import admin as admin_blueprint
# # app.register_blueprint(admin_blueprint, url_prefix='/admin')

# # from .auth import auth as auth_blueprint
# # app.register_blueprint(auth_blueprint)

# # from .home import home as home_blueprint
# # app.register_blueprint(home_blueprint)


# Views
# from app.views import *
# from blog.views import *
