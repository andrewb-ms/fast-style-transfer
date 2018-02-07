from flask import Flask, request, redirect, url_for, send_file #, flash
from werkzeug.utils import secure_filename
from subprocess import call
import os
import shutil
import glob
app = Flask(__name__)


UPLOAD_FOLDER = '/msshared/tensorflow/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def root():
    return 'Server is up.  Try /tensorflow/{la_muse,scream,wave,udnie,rain_princess,wreck}'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/tensorflow/la_muse', methods=['POST'])
def tensorflow_la_muse():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            #flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            #flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            #shutil.rmtree('/msshared/tensorflow/*')
            files = glob.glob('/msshared/tensorflow/*')
            for f in files:
                os.remove(f)
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            os.system('sh runtensorflow.sh')
            return send_file(os.path.join('/msshared/tfoutput/', filename), mimetype='image/' + os.path.splitext(filename)[1][1:])

    return 'Done'

@app.route('/tensorflow/scream', methods=['POST'])
def tensorflow_scream():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            #flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            #flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            #shutil.rmtree('/msshared/tensorflow/*')
            files = glob.glob('/msshared/tensorflow/*')
            for f in files:
                os.remove(f)
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            os.system('python evaluate.py --checkpoint /msshared/models/fastmodels/scream.ckpt --in-path /msshared/tensorflow/ --out-path /msshared/tfoutput/')
            return send_file(os.path.join('/msshared/tfoutput/', filename), mimetype='image/' + os.path.splitext(filename)[1][1:])

    return 'Done'

@app.route('/tensorflow/wave', methods=['POST'])
def tensorflow_wave():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            #flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            #flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            #shutil.rmtree('/msshared/tensorflow/*')
            files = glob.glob('/msshared/tensorflow/*')
            for f in files:
                os.remove(f)
            files = glob.glob('/msshared/tfoutput/*')
            for f in files:
                os.remove(f)
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            os.system('python evaluate.py --checkpoint /msshared/models/fastmodels/wave.ckpt --in-path /msshared/tensorflow/ --out-path /msshared/tfoutput/')
            return send_file(os.path.join('/msshared/tfoutput/', filename), mimetype='image/' + os.path.splitext(filename)[1][1:])

    return 'Done'

@app.route('/tensorflow/udnie', methods=['POST'])
def tensorflow_udnie():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            #flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            #flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            #shutil.rmtree('/msshared/tensorflow/*')
            files = glob.glob('/msshared/tensorflow/*')
            for f in files:
                os.remove(f)
            files = glob.glob('/msshared/tfoutput/*')
            for f in files:
                os.remove(f)
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            os.system('python evaluate.py --checkpoint /msshared/models/fastmodels/udnie.ckpt --in-path /msshared/tensorflow/ --out-path /msshared/tfoutput/')
            return send_file(os.path.join('/msshared/tfoutput/', filename), mimetype='image/' + os.path.splitext(filename)[1][1:])

    return 'Done'

@app.route('/tensorflow/rain_princess', methods=['POST'])
def tensorflow_rain_princess():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            #flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            #flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            #shutil.rmtree('/msshared/tensorflow/*')
            files = glob.glob('/msshared/tensorflow/*')
            for f in files:
                os.remove(f)
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            os.system('python evaluate.py --checkpoint /msshared/models/fastmodels/rain_princess.ckpt --in-path /msshared/tensorflow/ --out-path /msshared/tfoutput/')
            return send_file(os.path.join('/msshared/tfoutput/', filename), mimetype='image/' + os.path.splitext(filename)[1][1:])

    return 'Done'

@app.route('/tensorflow/wreck', methods=['POST'])
def tensorflow_wreck():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            #flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            #flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            #shutil.rmtree('/msshared/tensorflow/*')
            files = glob.glob('/msshared/tensorflow/*')
            for f in files:
                os.remove(f)
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            os.system('python evaluate.py --checkpoint /msshared/models/fastmodels/wreck.ckpt --in-path /msshared/tensorflow/ --out-path /msshared/tfoutput/')
            return send_file(os.path.join('/msshared/tfoutput/', filename), mimetype='image/' + os.path.splitext(filename)[1][1:])

    return 'Done'
