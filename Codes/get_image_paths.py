import os
from glob import glob

def get_image_paths(data_path, categories):
    num_categories = len(categories)

    train_image_paths = []
    test_image_paths = []

    train_labels = []
    test_labels = []

    for category in categories:

        image_paths = glob(os.path.join(data_path, 'train', category, '*.jpg'))
        for i in range(len(image_paths)):
            #print("1")
            train_image_paths.append(image_paths[i])
            train_labels.append(category)

        image_paths = glob(os.path.join(data_path, 'test', category, '*.jpg'))
        for i in range(len(image_paths)):
            #print("2")
            test_image_paths.append(image_paths[i])
            test_labels.append(category)
            #print('category: %s, test image: %s' % (category, image_paths[i]))
            #print(len(test_labels))

    return train_image_paths, test_image_paths, train_labels, test_labels
