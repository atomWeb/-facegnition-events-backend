import json
import boto3
import os
from utils import jsonify


def handler(event, context):

    print(event)
    jresp = {'data': 'Person created!'}
    print(jresp)
    return jsonify(jresp)
