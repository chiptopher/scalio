from scalio.app import db
from scalio.datasource.repository import Repository
from flask_restful import fields


class UserSettings(db.Model, Repository):

    __tablename__ = 'user_settings'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='user_settings')
    rolling_average_days = db.Column(db.Integer, nullable=False)

    def __init__(self, **kwargs):
        super(UserSettings, self).__init__(**kwargs)
        self.register(self)

    @classmethod
    def delete_all(cls):
        db.session.query(UserSettings).delete()

    @staticmethod
    def resource_fields():
        return {
            'rolling_average_days': fields.Integer
        }
