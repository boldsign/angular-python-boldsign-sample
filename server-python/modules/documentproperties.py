import json
from app import app
from flask import request
import requests
from os import environ


@app.route('/api/getDocumentProperties', methods=['GET'])
def DocumentProperties():
    url = environ.get('BASE_URL') + "v1/document/properties?documentId=" + \
        request.args.get('documentId')
    payload = {}
    headers = {'X-API-KEY': environ.get('API_KEY')}
    response = requests.request("GET", url, headers=headers, data=payload)

    return json.loads(response.text)
