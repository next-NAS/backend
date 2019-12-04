import os
import csv
from service.config import config

class LabelManager(object):

    def __init__(self, user_id, task_id, dataset_name):
        self._user_id = user_id
        self._task_id = task_id
        self._dataset_name = dataset_name
    
    def generate_label_csv(self):
        '''
            生成用于标记（文件名 - 类别）的csv文件
        '''
        dataset_root = os.path.join(config['UPLOAD_FOLDER'], self._user_id, self._task_id, self._dataset_name)
        class_dirs = [i for i in os.listdir(train_dir) if os.path.isdir(os.path.join(train_dir, i))]
        # 保存一个字典，用于类别的编码和解码
        self._class_dirs_with_code = dict(zip(len(class_dirs), class_dirs))
        with open(os.path.join(dataset_root, 'label.csv'), 'w') as csv_file:
            fieldnames = ['File Name', 'Label']
            writer = csv.DictWriter(train_csv, fieldnames=fieldnames)
            writer.writeheader()
            # 遍历每一个类别并写入（文件名 - 类别）
            for label_code, current_class in self._class_dirs_with_code.items():
                for image in os.listdir(os.path.join(train_dir, current_class)):
                    writer.writerow({'File Name': str(image), 'Label':label_code})

