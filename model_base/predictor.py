# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 10:32:40 2019

@author: naresh.gangiredd
"""

import os
import json
# from sklearn.externals import joblib
import flask
import boto3
import time
# import pyarrow
# from pyarrow import feather
#from boto3.s3.connection import S3Connection
#from botocore.exceptions import ClientError
#import pickle
# import modin.pandas as pd

import logging

#Define the path
prefix = '/opt/code/'
model_path = os.path.join(prefix, 'model')
logging.info("Model Path" + str(model_path))

## Load the model components
#logging.info("We should load model using pkl file here")
# regressor = joblib.load(os.path.join(model_path, 'Regx.pkl'))



# The flask app for serving predictions
app = flask.Flask(__name__)
@app.route('/ping', methods=['GET'])
def ping():
    # Check if the classifier was loaded correctly
    try:
        #regressor
        status = 200
        logging.info("Status : 200")
    except:
        status = 400
    return flask.Response(response= json.dumps(' '), status=status, mimetype='application/json' )

@app.route('/invocations', methods=['POST'])
def transformation():
    # Get input JSON data and convert it to a DF
    input_json = flask.request.get_json()
    logging.info(input_json)
    result = {"message": "Prediction"}
    
    resultjson = json.dumps(result)
    return flask.Response(response=resultjson, status=200, mimetype='application/json')
