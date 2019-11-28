import os

def get_size(path):
  size = 0
  for f in os.listdir(path):
    full_path = os.path.join(path, f)
    if os.path.isfile(full_path):
      size += os.path.getsize(full_path)
  return size

dataset_root = 'data/guest/dddd/MyDataset'
sample_names = os.listdir(dataset_root)
print(sample_names)
sample_size = [get_size(os.path.join(dataset_root, sample)) for sample in sample_names]
print(sample_size)