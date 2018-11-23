from datetime import timedelta

from scalio.app import db
from scalio.datasource.repository import Repository
from scalio.users.settings.model import UserSettings
from scalio.util.timestamp import time_in_millis


class User(db.Model, Repository):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    weighIns = db.relationship('WeighIn', back_populates='user')
    user_settings = db.relationship('UserSettings', uselist=False, back_populates='user')

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.user_settings = UserSettings(rolling_average_days=7)
        self.register(self)

    def __repr__(self):
        return "User(email='{}', passowrd='{}'".format(self.email, self.password)

    @classmethod
    def find_by_username(cls, username):
        return db.session.query(User).filter_by(email=username).first()

    @classmethod
    def delete_all(cls):
        db.session.query(User).delete()

    def get_weigh_in_average(self):
        sorted_weigh_ins = sorted(self.weighIns, key=lambda x: x.date, reverse=True)
        rolling_average_cutoff_timestamp = time_in_millis(delta=timedelta(days=self.user_settings.rolling_average_days))
        truncated_weigh_ins = [w for w in sorted_weigh_ins if w.date > rolling_average_cutoff_timestamp]
        result = 0
        try:
            result = sum(weigh_in.weight for weigh_in in truncated_weigh_ins) / len(truncated_weigh_ins)
        except ZeroDivisionError:
            pass
        return result
