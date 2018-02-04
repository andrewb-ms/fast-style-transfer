from flask import Flask, request, redirect, url_for, flash
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


@app.route('/tensorflow_la_muse_depracated')
def tensorflow_la_muse():
    #execfile("python /home/adm101/fast-style-transfer/evaluate.py --checkpoint /msshared/models/fastmodels/la_muse.ckpt --in-path /msshared/tensorflow/ --out-path /msshared/tfoutput/")
    #call(["python", "/home/adm101/fast-style-transfer/evaluate.py --checkpoint /msshared/models/fastmodels/la_muse.ckpt --in-path /msshared/tensorflow/ --out-path /msshared/tfoutput/"])
    os.system("python /home/adm101/fast-style-transfer/evaluate.py --checkpoint /msshared/models/fastmodels/la_muse.ckpt --in-path /msshared/tensorflow/ --out-path /msshared/tfoutput/")
    return 'Server is up'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/tensorflow_la_muse', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return 'Done'

