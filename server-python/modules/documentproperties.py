import json
from app import app
from flask import jsonify, request
import requests
from os import environ
import boldsign


@app.route('/api/getDocumentProperties', methods=['GET'])
def DocumentProperties():
    configuration = boldsign.Configuration(
    api_key = environ.get('API_KEY')
)

    with boldsign.ApiClient(configuration) as api_client:

        document_api = boldsign.DocumentApi(api_client)

        get_properties_response = document_api.get_properties(document_id=request.args.get('documentId'))

        return jsonify(get_properties_response.to_dict())