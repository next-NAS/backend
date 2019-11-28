from flask_restful import Resource
from flask import request
import os, json
from server.config import config

class TaskMetaData(Resource):

    def post(self, user_id, task_id):
        task_type = request.form['task_type']
        meta_file_location = os.path.join(config['UPLOAD_FOLDER'], user_id, task_id)
        meta = {}

        with open(os.path.join(meta_file_location, 'task_meta_data'), 'w') as f:
            meta['name'] = task_id
            meta['task_type'] = task_type

            dataset_info = {}
            dataset_info['name'] = self.get_dataset_name()
            samples_info = self.get_samples_info()
            dataset_info['size'] = sum([s['size'] for s in samples_info])
            dataset_info['nums'] = [s['num'] for s in samples_info]
            dataset_info['sample_num'] = sum(dataset_info['nums'])
            dataset_info['class_num'] = len(samples_info)
            dataset_info['classes'] = [s['class'] for s in samples_info]
            
            meta['dataset'] = dataset_info

            json.dump(meta, f)

        return meta, 200

