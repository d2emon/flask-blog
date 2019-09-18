import os


basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


class Config:
    ADMINS = ['admin@example.com']

    # Old -> DEBUG = False
    # Old -> TESTING = False

    # Log
    LOG_PATH = os.environ.get('LOG_PATH') or os.path.join(basedir, 'log')
    LOG_FILE = os.environ.get('LOG_FILE') or os.path.join(LOG_PATH, 'blog.log')
    # Old -> LOG = {
    # Old ->     "FILENAME": os.path.join(BASE_DIR, "log", "execom.log"),
    # Old ->     "MAX_BYTES": 1024 * 1024,
    # Old ->     "BACKUP_COUNT": 10,
    # Old ->     "FORMAT": "%(asctime)s[%(levelname)s]:\t%(message)s\tin %(module)s at %(lineno)d",
    # Old -> }

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
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Old -> STATIC_FOLDER = os.path.join(BASE_DIR, 'static')
    # Old -> TEMPLATE_FOLDER = os.path.join(BASE_DIR, 'templates')

    # Old -> UPLOAD_PATH = os.path.join(BASE_DIR, "upload")
    # Old -> # UPLOAD_FOLDER = './static/upload/'
    # Old -> # ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

    # Old -> VIEW_CASE = "edit_case"
