from flask import Flask, render_template
from subprocess import call

app = Flask(__name__)

@app.before_first_request
def compile_templates():
    # Compiling handlebars templates.
    call(["handlebars", "static/templates/", "-f", 
          "static/js/templates.js"])

@app.route('/')
def anime_recognizer():
    test_predictions = [{
        "image": "static/images/test_set/2402997.jpg", 
        "predictions":[
            {"name": "Suwako", "confidence": "90"}
        ]
    }, {
        "image": "static/images/test_set/11538747.jpg",
        "predictions":[
            {"name": "Miku Hatsune", "confidence": "80"},
            {"name": "Ren Kagamine", "confidence": "75"}
        ]
    }]

    return render_template('anime_recognizer.html', test_predictions=test_predictions)

if __name__ == "__main__":
    app.run(debug=True)
