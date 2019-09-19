import logging
import os


class Config:
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

    ADMINS = ['admin@example.com']

    # Old -> DEBUG = False
    # Old -> TESTING = False

    # Log
    LOG_FILE_BACKUP_COUNT = os.environ.get('LOG_FILE_BACKUP_COUNT') or 10
    LOG_FILE_MAX_BYTES = os.environ.get('LOG_FILE_MAX_BYTES') or 1024 * 1024
    LOG_FILENAME = os.environ.get('LOG_FILENAME') or os.path.join(BASE_DIR, 'log', 'blog.log')
    LOG_HANDLERS = {
        'FILE': {
            'formatter': logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'),
        },
        'MAIL': {},
    }
    LOG_LEVEL = logging.INFO
    LOG_MAIL_SUBJECT = "Blog Failure"

    # Mail
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT') or 25
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    # Pagination
    POSTS_PER_PAGE = 25
    # Old -> RECORDS_ON_PAGE = 50
    # Old -> # PER_PAGE = 10

    # Secret key
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'blog-secret-key'

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(BASE_DIR, 'db', 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Old -> STATIC_FOLDER = os.path.join(BASE_DIR, 'static')
    # Old -> TEMPLATE_FOLDER = os.path.join(BASE_DIR, 'templates')

    # Old -> UPLOAD_PATH = os.path.join(BASE_DIR, "upload")
    # Old -> # UPLOAD_FOLDER = './static/upload/'
    # Old -> # ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

    # Old -> VIEW_CASE = "edit_case"
