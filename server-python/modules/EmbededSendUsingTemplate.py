import json
from app import app
from flask import request
import requests
from os import environ
import boldsign


@app.route('/api/template/createEmbeddedRequestUrl', methods=['POST'])
def EmbeddedSendUsingTemplate():
    configuration = boldsign.Configuration(
    api_key = environ.get('API_KEY')
)   
    with boldsign.ApiClient(configuration) as api_client:
    
        template_api = boldsign.TemplateApi(api_client)
        data = json.loads(request.data)

        role = boldsign.Role(
            roleIndex=1,
            role = "Manager",
            signerName= data['name'],
            signerEmail= data['email'],
        )
        
        embedded_send_template_form_requests = boldsign.EmbeddedSendTemplateFormRequest(
            title="API template",
            message= "This Template Document from API",
            roles=[role],        
            showToolbar=True,
            sendViewOption= "PreparePage",
            redirectUrl= "http://localhost:4200/embedDocument/completed",
        )
        
        create_embedded_request_url_template_response = template_api.create_embedded_request_url_template(
            template_id= data['templateId'],
            embedded_send_template_form_request=embedded_send_template_form_requests
        )
        return json.loads(json.dumps(create_embedded_request_url_template_response.to_dict()))
