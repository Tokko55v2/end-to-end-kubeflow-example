#!flask/bin/python
import os
from flask import Flask, jsonify, render_template, request, url_for

app = Flask(__name__)

@app.route('/predict')
def predict():
        return render_template('predict.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    if os.environ['ENVIRONMENT'] == 'local':
        app.run(port = 5000, host = '0.0.0.0')
