""" Builds a test set by picking one random image for each character.
"""
import cPickle as pickle
import sys
import numpy as np
import shutil
import os.path

if __name__ == "__main__":
    if len(sys.argv) < 6:
        raise ValueError("Please input a pickle file for test data, an input folder for images, an input folder for JSON files,  an output folder for images and another for JSON files.")
    test_fname = sys.argv[1]
    img_in_folder = sys.argv[2]
    json_in_folder = sys.argv[3]
    img_out_folder = sys.argv[4]
    json_out_folder = sys.argv[5]
    test_set = pickle.load(open(test_fname, 'rb'))
    img_per_tag = {}

    for fname in test_set:
        for label in test_set[fname]:
            if label in img_per_tag:
                img_per_tag[label].append(fname)
            else:
                img_per_tag[label] = []

    for label in img_per_tag:
        nb_images = len(img_per_tag[label])
        rand_idx = np.random.randint(nb_images)
        base_fname = os.path.splitext(img_per_tag[label][rand_idx])[0]
        shutil.copy(os.path.join(img_in_folder, base_fname.decode('utf-8') + '.jpg'),
                    img_out_folder)
        shutil.copy(os.path.join(json_in_folder, base_fname.decode('utf-8') + '.json'),
                    json_out_folder)
