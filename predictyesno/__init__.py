#The following 3 lines are necessary to be run before importing flask to avoid the error:
#    from werkzeug import cached_property
#ImportError: cannot import name 'cached_property'
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask import Flask, request, render_template, flash, jsonify
import logging, sys, os
from . import forms
from flask_cors import CORS
logging.basicConfig(level=logging.INFO)
flask_app = Flask(__name__, static_folder="../build/static")
CORS(flask_app)


@flask_app.route('/')
def hello():
    with open("build/index.html", "rt") as h:
       return h.read()


@flask_app.route('/<filebasename>')
def manifest(filebasename):
    bnext = os.path.splitext(filebasename)
    if bnext[1].lower() in (".html", ".htm", ",js"):
        mode = "rt"
    else:
        mode = "rb"
    with open(os.path.join("build", filebasename), mode) as h:
       return h.read()


@flask_app.route('/train')
def train():
    tmodel = dataset.testmodel(dataset.MLPClassifier, max_iter=dataset.MAX_ITER, hidden_layer_sizes=dataset.HIDDEN_LAYER_SIZES)
    tmodel["status"] = "ok"
    return tmodel


@flask_app.route("/api/form", methods=["GET", "POST"])
@flask_app.route("/form", methods=["GET", "POST"])
def form():
    "That endpoint was used to serve the form HTML until we copied the served form code to ReactJS"
    frm = forms.TrialForm(request.form)
    if request.method == 'POST':
        if frm.validate():
            prediction = dataset.predict_from_dict(frm.data)
            return jsonify({
                "status": "ok",
                "prediction": prediction,
            })
        else:
        #    #There were misfilled fields - return to the form
            return jsonify({
                "status": "error",
                "prediction": frm.errors,
            })
    else:
        #This endpoint is no longer used as it has been translated to ReactJS
        rtempl = render_template("predictform.html", form=frm)
        return jsonify({"status": "ok", "formHTML": rtempl})
from . import dataset