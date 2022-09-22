import json
from app import app
from flask import request
import requests
from os import environ


@app.route('/api/template/send', methods=['POST'])
def sendDocumentUsingTemplate():
    url = environ.get('BASE_URL') + \
        "v1/template/send?templateId=" + request.json['templateId']
    payload = json.dumps({"title": "Template Document from API", "message": "This Template Document from API", "roles": [
        {
            "roleIndex": 1,
            "signerName": request.json['name'],
            "signerEmail": request.json['email'],
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
