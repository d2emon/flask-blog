import json
from app import db
from datetime import datetime


class Notification(db.Model):
    notification_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    payload = db.Column(db.Text)

    def get_data(self):
        return json.loads(str(self.payload))
