import json
from app import app
from flask import request
import requests
from os import environ


@app.route('/api/template/createEmbeddedRequestUrl', methods=['POST'])
def EmbeddedSendUsingTemplate():
    data = json.loads(request.data)
    url = environ.get(
        'BASE_URL') + "v1/template/createEmbeddedRequestUrl?templateId=" + data['templateId']
    payload = json.dumps({
        "title": "Template Document from API",
        "redirectUrl": "http://localhost:4200/embedDocument/completed",
        "message": "This Template Document from API",
        "sendViewOption": "PreparePage",
        "showToolbar": True,
        "roles": [
            {
                "roleIndex": 1,
                "signerName": data['name'],
                "signerEmail": data['email'],
                "role": "Manager"
            }
        ]
    })
    headers = {
        'X-API-KEY': environ.get('API_KEY'),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return json.loads(response.text)
