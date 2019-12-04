import os
import autokeras as ak
from autokeras.image.image_supervised import load_image_dataset
from autokeras.image.image_supervised import ImageClassifier
import service.config as config

class Trainer(object):

    def __init__(self, user_id, task_id, dataset_name):
        self._user_id = user_id
        self._task_id = task_id
        self._dataset_name = dataset_name
    
    def train(self):
        dataset_root = os.path.join(config.UPLOAD_FOLDER, 
                                    str(self._user_id), 
                                    str(self._task_id), 
                                    str(self._dataset_name))
        X, y = load_image_dataset(csv_file_path=os.path.join(dataset_root, config.LABEL_FILE_NAME),
                                    images_path=dataset_root)
        
        clf = ImageClassifier(verbose=True)
        clf.fit(X, y, time_limit=10 * 60 * 60)


