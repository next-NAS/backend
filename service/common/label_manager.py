import os
import csv
import service.config as config

class LabelManager(object):

    def __init__(self, user_id, task_id, dataset_name):
        self._user_id = user_id
        self._task_id = task_id
        self._dataset_name = dataset_name
    
    def generate_label_csv(self):
        '''
            生成用于标记（文件名 - 类别）的csv文件
        '''
        dataset_root = os.path.join(config.UPLOAD_FOLDER, 
                                    str(self._user_id), 
                                    str(self._task_id), 
                                    str(self._dataset_name))
        class_dirs = [i for i in os.listdir(dataset_root) if os.path.isdir(os.path.join(dataset_root, i))]
        # 保存一个字典，用于类别的编码和解码
        self._class_dirs_with_code = dict(zip( range(len(class_dirs)) , class_dirs))

        with open(os.path.join(dataset_root, config.LABEL_FILE_NAME), 'w') as csv_file:
            fieldnames = ['File Name', 'Label']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            # 遍历每一个类别并写入（文件名 - 类别）
            for label_code, current_class in self._class_dirs_with_code.items():
                # 遍历单个类别文件
                for sample_name in os.listdir(os.path.join(dataset_root, current_class)):
                    writer.writerow({'File Name': os.path.join(current_class, str(sample_name)), 
                                    'Label':label_code})

