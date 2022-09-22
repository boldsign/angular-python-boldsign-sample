import json
from app import app
from flask import request
from os import environ
import requests


@app.route('/api/embedSigning', methods=['POST'])
def EmbeddedSigning():
    url = environ.get('BASE_URL') + "v1/template/send?templateId=" + \
        request.json['templateId']
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
    docId = json.loads(response.text)['documentId']
    signLink = getEmbeddedSigningLink(docId, request.json['email'])
    data = json.dumps({'documentId': docId, 'signLink': signLink})
    return json.loads(data)


def getEmbeddedSigningLink(docId, email):
    url = environ.get('BASE_URL') + "v1/document/getEmbeddedSignLink?documentId=" + docId + \
        "&signeremail=" + email + "&redirectUrl=http://localhost:4200/embedDocument/completed"
    payload = {}
    headers = {
        'X-API-KEY': environ.get('API_KEY')
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return json.loads(response.text)['signLink']
