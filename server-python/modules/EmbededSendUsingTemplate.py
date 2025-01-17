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
        form_fields = [
            boldsign.FormField(
                fieldType="Signature",
                page_number=1,
                bounds=boldsign.Rectangle(
                    x=50,
                    y=100,
                    width=100,
                    height=60
                )
            )
        ]

        role = boldsign.Role(
            roleIndex=2,
            role = "Manager",
            signerRole="signer",
            signerName= data['name'],
            signerEmail= data['email'],
            formFields=form_fields
        )
        
        embedded_send_template_form_requests = boldsign.EmbeddedSendTemplateFormRequest(
            title="API template",
            message= "This Template Document from API",
            allowMessageEditing=True,    
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