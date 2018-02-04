from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
from subprocess import call
import os
app = Flask(__name__)


UPLOAD_FOLDER = '/msshared/tensorflow/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def root():
    return 'Server is up'


@app.route('/tensorflow_la_muse')
def tensorflow_la_muse():
    #execfile("python /home/adm101/fast-style-transfer/evaluate.py --checkpoint /msshared/models/fastmodels/la_muse.ckpt --in-path /msshared/tensorflow/ --out-path /msshared/tfoutput/")
    #call(["python", "/home/adm101/fast-style-transfer/evaluate.py --checkpoint /msshared/models/fastmodels/la_muse.ckpt --in-path /msshared/tensorflow/ --out-path /msshared/tfoutput/"])
    os.system("python /home/adm101/fast-style-transfer/evaluate.py --checkpoint /msshared/models/fastmodels/la_muse.ckpt --in-path /msshared/tensorflow/ --out-path /msshared/tfoutput/")
    return 'Server is up'



