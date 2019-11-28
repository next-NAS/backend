from flask import Flask
from flask_restful import Api
from service.resources.dataset import Dataset
from service.resources.task_metadata import TaskMetaData


app = Flask(__name__)
api = Api(app)

api.add_resource(Dataset, '/<string:user_id>/<string:task_id>/dataset')
api.add_resource(TaskMetaData, '/<string:user_id>/<string:task_id>/task-metadata')