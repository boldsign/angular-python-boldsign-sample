import json
from app import app
from flask import request
import requests
import os
from os import environ
import boldsign


@app.route('/api/document/createEmbeddedRequestUrl', methods=['POST'])
def EmbeddedSendDocument():
    configuration = boldsign.Configuration(
    api_key = environ.get('API_KEY')
)

    with boldsign.ApiClient(configuration) as api_client:
    
        document_api = boldsign.DocumentApi(api_client)

        file_dir = os.path.dirname(os.path.realpath('__file__'))
        file_name = os.path.join(file_dir, 'modules/Affidavit-of-Residence.pdf')
    
        form_fields = [
            boldsign.FormField(
                fieldType="Signature",
                pageNumber=1,
                bounds=boldsign.Rectangle(
                    x=50,
                    y=50,
                    width=200,
                    height=30
                )
            )
        ] 
        
        document_signer = boldsign.DocumentSigner(
            name=request.form["Name"],
            emailAddress=request.form["Email"],
            signerOrder=1,
            signerType="Signer",
        )
        
        embedded_document_request = boldsign.EmbeddedDocumentRequest(
            title="Sent from API Python SDK",
            redirectUrl="http://localhost:4200/embedDocument/completed",
            message="This is document message sent from API Python SDK",
            signers=[document_signer],
            sendViewOption='PreparePage',
            showToolbar=True,
            files=[file_name],  
            expiryDays=60,
            form_fields=form_fields      
        )
        
        embedded_request_url_document_response = document_api.create_embedded_request_url_document(
            embedded_document_request=embedded_document_request
        )
        return json.loads(json.dumps(embedded_request_url_document_response.to_dict()))
