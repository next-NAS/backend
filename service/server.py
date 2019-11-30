from flask import Flask
from flask_restful import Api
from service.resources.dataset import Dataset
from service.resources.tasks import Tasks


app = Flask(__name__)
api = Api(app)

api.add_resource(Dataset, '/<string:user_id>/<string:task_id>/dataset')
api.add_resource(Tasks, '/<string:user_id>/tasks')