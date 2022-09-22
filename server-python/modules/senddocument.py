import json
from app import app
from flask import request
import requests
import os
from os import environ


@app.route('/api/document/send', methods=['POST'])
def sendDocument():
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    file_name = os.path.join(file_dir, 'modules/Affidavit-of-Residence.pdf')
    url = environ.get('BASE_URL') + "v1/document/send"
    signers = {"name": request.form["Name"], "emailAddress": request.form["Email"], "signerOrder": 1, "formFields": [
        {"isRequired": True, "fieldType": "Signature", "name": "Sign", "pageNumber": 1, "bounds": {"width": 200, "height": 30, "x": 20, "y": 30}}]}
    payload = {
        'Message': 'test',
        'Signers': json.dumps(signers),
        'ExpiryDays': '60',
        'Title': 'test'
    }
    files = [('Files', ('file', open(
        file_name, 'rb'), 'application/pdf'))]
    headers = {'accept': 'application/json',
               'X-API-KEY': environ.get('API_KEY')
               }
    response = requests.request(
        "POST", url, headers=headers, data=payload, files=files)
    return json.loads(response.text)
