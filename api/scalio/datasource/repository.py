from scalio.app import db


class Repository:

    @classmethod
    def delete_all(cls):
        raise NotImplementedError

    @classmethod
    def register(cls, entity):
        db.session.add(entity)
        db.session.commit()

    def remove(self):
        db.session.delete(self)
        db.session.commit()
