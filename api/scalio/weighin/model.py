from flask_restful import fields

from scalio.app import db
from scalio.datasource.repository import Repository


class WeighIn(db.Model, Repository):
    @classmethod
    def delete_all(cls):
        db.session.query(WeighIn).delete()
        db.session.commit()

    __tablename__ = 'weighin'

    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Float, nullable=False)
    date = db.Column(db.Numeric(20, asdecimal=False), nullable=False)  # Time created as a timestamp
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='weighIns')

    def __init__(self, **kwargs):
        super(WeighIn, self).__init__(**kwargs)
        self.register(self)

    def __repr__(self):
        return "WeighIn(id='{}', weight='{}', data='{}')".format(self.id, self.weight, self.date)

    @classmethod
    def find_by_id(cls, id):
        return db.session.query(WeighIn).filter_by(id=id).first()

    @classmethod
    def find_all_user(cls, user):
        return db.session.query(WeighIn).filter_by(user=user).all()

    @staticmethod
    def resource_fields():
        return {
            'id': fields.Integer,
            'weight': fields.Float,
            'date': fields.Integer,
        }
