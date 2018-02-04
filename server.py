from flask import Flask
from subprocess import call
import os
app = Flask(__name__)

@app.route('/')
def root():
    return 'Server is up'


@app.route('/tensorflow_la_muse')
def tensorflow_la_muse():
    #execfile("python /home/adm101/fast-style-transfer/evaluate.py --checkpoint /msshared/models/fastmodels/la_muse.ckpt --in-path /msshared/tensorflow/ --out-path /msshared/tfoutput/")
    #call(["python", "/home/adm101/fast-style-transfer/evaluate.py --checkpoint /msshared/models/fastmodels/la_muse.ckpt --in-path /msshared/tensorflow/ --out-path /msshared/tfoutput/"])
    os.system("python /home/adm101/fast-style-transfer/evaluate.py --checkpoint /msshared/models/fastmodels/la_muse.ckpt --in-path /msshared/tensorflow/ --out-path /msshared/tfoutput/")
    return 'Server is up'



