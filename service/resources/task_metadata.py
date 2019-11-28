from flask_restful import Resource
from flask import request
import os, json
from service.config import config

class TaskMetaData(Resource):

    def post(self, user_id, task_id):
        data = request.get_json(force=True)
        task_type = data['task_type']
        dataset_name = data['dataset_name']
        meta_file_location = os.path.join(config['UPLOAD_FOLDER'], user_id, task_id)
        meta = {}

        with open(os.path.join(meta_file_location, 'task_meta_data'), 'w') as f:
            meta['name'] = task_id
            meta['task_type'] = task_type

            dataset_info = {}
            dataset_info['name'] = dataset_name
            # get_samples_info返回一个由'suze'、'num'、'class'组成的字典的列表
            samples_info = self.get_samples_info(os.path.join(meta_file_location, dataset_name))
            dataset_info['size'] = sum([s['size'] for s in samples_info])
            dataset_info['nums'] = [s['num'] for s in samples_info]
            dataset_info['sample_num'] = sum(dataset_info['nums'])
            dataset_info['class_num'] = len(samples_info)
            dataset_info['classes'] = [s['class'] for s in samples_info]
            
            meta['dataset'] = dataset_info

            json.dump(meta, f)

        return meta, 200

    def get_samples_info(self, dataset_root):
        '''
            返回一个由{'size': xx, 'num': xx, 'class': xx}组成的列表
            其中，size指的是子文件夹大小，num指的是样本数量，class指的是样本类别（即子文件名）
        '''
        sample_names = os.listdir(dataset_root)
        sample_size = [self.dir_size(os.path.join(dataset_root, sample)) for sample in sample_names]
        sample_num = [self.file_counts(os.path.join(dataset_root, sample)) for sample in sample_names]
        return [{'class': sample_names[i], 'size': sample_size[i], 'num': sample_num[i]} \
                    for i in range(len(sample_names))]

    def dir_size(self, path):
        size = 0
        for f in os.listdir(path):
            full_path = os.path.join(path, f)
            if os.path.isfile(full_path):
                size += os.path.getsize(full_path)
        return size
    

    def file_counts(self, path):
        return len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])