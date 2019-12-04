from service.common.label_manager import LabelManager

def test_label_manager():
    lm = LabelManager(user_id='guest', task_id='example_task', dataset_name='MyDataset')
    lm.generate_label_csv(label_filename='label.csv')

if __name__ == '__main__':
    test_label_manager()
