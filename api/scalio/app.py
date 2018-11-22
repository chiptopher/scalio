from flask import Flask
from flask_restful import Resource, Api
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from scalio.util.env import env


import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

app = Flask(__name__)
# A mysql connection string would look something like this: mysql+mysqlconnector://root:password@localhost/mydatabase
app.config['SQLALCHEMY_DATABASE_URI'] = env.database_url

CORS(app)

api = Api(app)
db = SQLAlchemy(app)


@app.after_request
def commit(response):
    db.session.commit()
    return response


@app.before_first_request
def create_tables():
    db.create_all()


class Ping(Resource):
    def get(self):
        return None, 200


from scalio.users.controller import UserRegistration, UserLogin, UserAuthenticationApi
from scalio.weighin.controller import WeighInResource, IndividualWeighIn
from scalio.users.settings.controller import IndividualSettingsApi
from scalio.weighin.calculation.controller import CalculationAverageResource
api.add_resource(Ping, '/api')
api.add_resource(UserRegistration, '/api/user/register')
api.add_resource(UserLogin, '/api/user/login')
api.add_resource(WeighInResource, '/api/weighin')
api.add_resource(IndividualWeighIn, '/api/weighin/<int:id>')
api.add_resource(IndividualSettingsApi, '/api/user/settings')
api.add_resource(UserAuthenticationApi, '/api/user/authenticated')
api.add_resource(CalculationAverageResource, '/api/weighin/calculation/average')
