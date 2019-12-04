import autokeras as ak
from autokeras.image.image_supervised import load_image_dataset
from autokeras.image.image_supervised import ImageClassifier

x_train, y_train = load_image_dataset(csv_file_path="./data/guest/example_task/chest_xray/label.csv",
                                      images_path="./data/guest/example_task/chest_xray/")

clf = ImageClassifier(verbose=True)
clf.fit(x_train, y_train, time_limit=10 * 60 * 60)
