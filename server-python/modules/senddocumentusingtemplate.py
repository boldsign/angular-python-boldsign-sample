import json
from app import app
from flask import jsonify, request
import requests
from os import environ
import boldsign

@app.route('/api/template/send', methods=['POST'])
def sendDocumentUsingTemplate():
    configuration = boldsign.Configuration(
    api_key = environ.get('API_KEY')
    )

    with boldsign.ApiClient(configuration) as api_client:

        template_api = boldsign.TemplateApi(api_client)

        role = boldsign.Role(
            role_index=1,
            signer_name= request.json['name'],
            signer_email= request.json['email'],
            role = "Manager"
        )

        template_id = request.json['templateId']

        send_for_sign_from_template = boldsign.SendForSignFromTemplateForm(
            title="Invitation form",
            message="Kindly review and sign this.",
            roles=[role],
        )

        send_using_template_response = template_api.send_using_template(template_id, send_for_sign_from_template)

        return jsonify(send_using_template_response.to_dict())
