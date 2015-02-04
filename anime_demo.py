from flask import Flask, render_template
from subprocess import call
import cPickle as pickle
import numpy as np
import os
import os.path
import cv2

from cnn_anime.dataset import ListDataset

# Load the prediction model.
def load_model():
    cnn = None
    with open('models/gap19_spp_thresh.pkl', 'rb') as cnn_file:
        cnn = pickle.load(cnn_file)
    return cnn
model = load_model()

def identify(image):
    """ Identifies the anime characters in an image.

    Arguments:
        image
            image to recognize characters from.
    """
    labels = model.predict_labels_named(
        ListDataset([image], [frozenset([])]),
        batch_size=1,
        method='thresh',
        confidence=True
    )
    conf_dict = []
    max_conf = np.max(map(lambda l: l[1], labels[0]))

    for label, conf in labels[0]:
        conf_dict.append({
            'name': label,
            'confidence': conf / max_conf * 100
        })
        
    return sorted(conf_dict, key=lambda p: p['confidence'], reverse=True)

def test_predict():
    """ Runs prediction on the test set.
    """
    print "Running prediction on the test set..."
    image_dir = 'static/images/test_set'
    img_fnames = [f for f in os.listdir(image_dir) if f.endswith('.jpg')]
    predictions = []

    for img_fname in img_fnames:
        image = cv2.imread(os.path.join(image_dir, img_fname))
        predictions.append({
            "image": os.path.join(image_dir, img_fname),
            "predictions": identify(image)
        })
    print "Prediction done!"
    return predictions

test_predictions = test_predict()

app = Flask(__name__)

@app.route('/')
def anime_recognizer():
    randidx = np.random.permutation(len(test_predictions))
    displayed_predictions = [test_predictions[i] for i in randidx[0:16]]

    return render_template('anime_recognizer.html', test_predictions=displayed_predictions)

if __name__ == "__main__":
    app.run(debug=True)
