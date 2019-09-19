from app import app, db
from datetime import datetime
from flask import g
from flask_babel import get_locale
from flask_login import current_user


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

    g.locale = str(get_locale())
