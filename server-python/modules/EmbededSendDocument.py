import json
from app import app
from flask import request
import requests
import os
from os import environ


@app.route('/api/document/createEmbeddedRequestUrl', methods=['POST'])
def EmbeddedSendDocument():
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    file_name = os.path.join(file_dir, 'modules/Affidavit-of-Residence.pdf')
    url = environ.get('BASE_URL') + "v1/document/createEmbeddedRequestUrl"
    signers = {"name": request.form["Name"],
               "emailAddress": request.form["Email"], "signerType": 1}
    payload = {
        'Message': 'test',
        'Signers': json.dumps(signers),
        'ExpiryDays': '60',
        'Title': 'test',
        'SendViewOption': 'PreparePage',
        'ShowToolbar': 'true',
        'RedirectUrl': 'http://localhost:4200/embedDocument/completed'
    }
    files = [('Files', ('file', open(
        file_name, 'rb'), 'application/pdf'))]
    headers = {'accept': 'application/json',
               'X-API-KEY': environ.get('API_KEY')
               }
    response = requests.request(
        "POST", url, headers=headers, data=payload, files=files)
    return json.loads(response.text)
