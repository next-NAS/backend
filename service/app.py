from flask import Flask
from flask_restful import Api
from service.resources.dataset import Dataset


app = Flask(__name__)
api = Api(app)

api.add_resource(Dataset, '/automl/<string:task_type>/<string:user_id>/<string:task_id>/dataset')
