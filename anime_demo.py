# -*- coding: utf-8 -*-
from flask import Flask, g, session, request, render_template, jsonify, abort
from flask.ext.babel import Babel, get_locale
import numpy as np
import cPickle as pickle
import numpy as np
import os
import os.path
import json
import copy
from skimage.transform import resize
from skimage.io import imread, imshow
import PIL
import StringIO

from cnn_anime.dataset import ListDataset
from label_translate import label_to_english, label_to_japanese
from messages_en import messages_en
from messages_ja import messages_ja
from secret_key import secret_key

""" Setup priori to launching the app. Prepares the prediction model, etc.
"""

# Load the prediction model.
model = None
test_predictions = None

def load_model():
    cnn = None
    with open('models/gap19_spp_thresh.pkl', 'rb') as cnn_file:
        cnn = pickle.load(cnn_file)
    return cnn

def identify(image):
    """ Identifies the anime characters in an image.

    Arguments:
        image
            image to recognize characters from. Should be in (row, cols, channels) shape,
            BGR format, 8-bit depth.
    """
    assert image.dtype == np.uint8
    assert image.shape[2] == 3
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
    img_resized = (resize(image, (n_rows, n_cols)) * 255).astype(np.uint8)
    print (img_resized.dtype, img_resized.shape, img_resized.min(), img_resized.max(), img_resized.mean())
    labels = model.predict_labels_named(
        ListDataset([img_resized], [frozenset([])]),
        batch_size=1,
        method='thresh',
        confidence=True
    )
    conf_dict = []
    max_conf = np.max(map(lambda l: l[1], labels[0]))

    # Translate according the locale.
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
    json_dir = 'cc-anime-images/info'
    img_fnames = [f for f in os.listdir(image_dir) if f.endswith('.jpg')]
    predictions = []
    license_names = {
        'cc-3.0': "CC BY 3.0",
        'cc-sa-3.0': "CC BY-SA 3.0",
        'cc-nd-3.0': "CC BY-ND 3.0",
        'cc-nc-3.0': "CC BY-NC 3.0",
        'cc-nc-sa-3.0': "CC BY-NC-SA 3.0",
        'cc-nc-nd-3.0': "CC BY-NC-ND 3.0"
    }
    license_urls = {
        'cc-3.0': "http://creativecommons.org/licenses/by/3.0/",
        'cc-sa-3.0': "http://creativecommons.org/licenses/by-sa/3.0/",
        'cc-nd-3.0': "http://creativecommons.org/licenses/by-nd/3.0/",
        'cc-nc-3.0': "http://creativecommons.org/licenses/by-nc/3.0/",
        'cc-nc-sa-3.0': "http://creativecommons.org/licenses/by-nc-sa/3.0/",
        'cc-nc-nd-3.0': "http://creativecommons.org/licenses/by-nc-nd/3.0/"
    }

    for img_fname in img_fnames:
        image = imread(os.path.join(image_dir, img_fname))
        image_bgr = np.array(image, copy=True)
        image_bgr[:,:,0] = image[:,:,2]
        image_bgr[:,:,2] = image[:,:,1]
        base_name = os.path.splitext(os.path.basename(img_fname))[0]
        image_info = None
        with open(os.path.join(json_dir, base_name + '.json')) as json_file:
            image_info = json.load(json_file)
        predictions.append({
            "image": os.path.join(image_dir, img_fname),
            "predictions": identify(image_bgr),
            "illust_info": None if image_info is None else {
                "title": image_info["title"],
                "author": image_info["author"],
                "url": image_info["url"],
                "license-name": license_names[image_info["license_type"]],
                "license-url": license_urls[image_info["license_type"]]
            }
        })
    print "Prediction done!"
    return predictions

def init_everything():
    global test_predictions
    global model
    model = load_model()
    test_predictions = test_predict()

if os.environ.get('WERKZEUG_RUN_MAIN'):
    # Werkzeug sets this environment variable for the actual server process. So we only
    # run the initialization code in that case.
    init_everything()

app = Flask(__name__)
babel = Babel(app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'ja'])

@app.route('/', methods=['GET'])
def anime_recognizer():
    new_locale = request.args.get('locale', None)
    if new_locale is not None:
        session['locale'] = new_locale
    elif 'locale' not in session:
        session['locale'] = request.accept_languages.best_match(['en', 'ja'])
    randidx = np.random.permutation(len(test_predictions))
    displayed_predictions = copy.deepcopy([test_predictions[i] for i in randidx[0:16]])
    # Localizing label names.
    label_tr = label_to_japanese if session['locale'] == 'ja' else label_to_english
    
    for img in displayed_predictions:
        for pred in img['predictions']:
            pred['name'] = label_tr[pred['name']]

    return render_template(
        'anime_recognizer.html',
        test_predictions=displayed_predictions,
        **(messages_ja if session['locale'] == 'ja' else messages_en)
    )

@app.route('/identify_upload', methods=['POST'])
def identify_handler():
    if request.method == 'POST':
        # Get the uploaded image.
        img_file = request.files['file']
        print "to stringio"
        img_stringio = StringIO.StringIO(img_file.stream.read())
        print "to PIL"
        image_pil = PIL.Image.open(img_stringio, mode='r')
        print "to numpy"
        print image_pil.shape
        image = np.asarray(image_pil, dtype=np.uint8)
        if image is None or image.shape[2] > 3 or image.shape[0] > 1024 or image.shape[1] > 1024:
            abort(400)
        # If all went well, feed it to the model for identification.
        results = identify(image)
        label_tr = label_to_japanese if session['locale'] == 'ja' else label_to_english
        for pred in results:
            pred['name'] = label_tr[pred['name']]
        
        return jsonify({'results': results})

app.secret_key = secret_key

if __name__ == "__main__":
    app.run(debug=True)
