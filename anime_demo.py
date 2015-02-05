# -*- coding: utf-8 -*-
from flask import Flask, g, request, render_template, jsonify, abort
from flask.ext.babel import Babel, gettext
from subprocess import call
import cPickle as pickle
import numpy as np
import os
import os.path
import cv2

from cnn_anime.dataset import ListDataset

""" Setup priori to launching the app. Prepares the prediction model, etc.
"""
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
    # Resize the image.
    rows, cols = image.shape[0:2]
    n_rows, n_cols = (None, None)
    min_dim = 256
    max_nb_pred = 5
    
    if rows > cols:
        n_rows = int(round(min_dim * float(rows) / cols))
        n_cols = min_dim
    else:
        n_cols = int(round(min_dim * float(cols) / rows))
        n_rows = min_dim
    img_resized = cv2.resize(image, (n_cols, n_rows), interpolation=cv2.INTER_AREA)
    labels = model.predict_labels_named(
        ListDataset([img_resized], [frozenset([])]),
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
        
    return sorted(conf_dict, key=lambda p: p['confidence'], reverse=True)[0:max_nb_pred]

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
babel = Babel(app)

@babel.localeselector
def get_locale():
    # The user can select a locale in the navbar, which we store here.
    selected_locale = getattr(g, 'locale', None)
    if selected_locale is None:
        return selected_locale
    else:
        # Otherwise, smart guess between English and Japanese.
        return request.accept_languages.best_match(['en', 'ja'])

@app.route('/')
def anime_recognizer():
    randidx = np.random.permutation(len(test_predictions))
    displayed_predictions = [test_predictions[i] for i in randidx[0:16]]

    return render_template('anime_recognizer.html', test_predictions=displayed_predictions)

@app.route('/identify_upload', methods=['POST'])
def identify_handler():
    if request.method == 'POST':
        # Get the uploaded image.
        img_file = request.files['file']
        img_raw = np.fromstring(img_file.stream.read(), dtype=np.uint8)
        image = cv2.imdecode(img_raw, 1)
        if image is None:
            abort(400)
        # If all went well, feed it to the model for identification.
        results = identify(image)
        
        return jsonify({'results': results})

if __name__ == "__main__":
    app.run(debug=True)
