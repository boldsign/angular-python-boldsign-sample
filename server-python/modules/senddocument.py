import json
from app import app
from flask import jsonify, request
import os
from os import environ
import boldsign

@app.route('/api/document/send', methods=['POST'])
def sendDocument():
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    file_name = os.path.join(file_dir, 'modules/Affidavit-of-Residence.pdf')
    configuration = boldsign.Configuration(
    api_key = environ.get('API_KEY')
    )

    with boldsign.ApiClient(configuration) as api_client:

        document_api = boldsign.DocumentApi(api_client)

        form_fields = [
            boldsign.FormField(
                fieldType="Signature",
                pageNumber=1,
                bounds=boldsign.Rectangle(
                    x=50,
                    y=50,
                    width=200,
                    height=25
                )
            ),
            boldsign.FormField(
                fieldType="Label",
                value="Label Field",
                pageNumber=1,
                bounds=boldsign.Rectangle(
                    x=150,
                    y=250,
                    width=200,
                    height=25
                )
            ),
        ]

        document_signer = boldsign.DocumentSigner(
            name=request.form["Name"],
            emailAddress=request.form["Email"],
            signerOrder=1,
            signerType="Signer",
            formFields=form_fields,
            locale="EN"
        )

        send_for_sign = boldsign.SendForSign(
            document_title = "SDK Document Test case",
            files=[file_name],
            message='Please sign this.',
            signers=[document_signer],
            title="Document SDK API test",
            expiryDateType='Days',
            expiryDate=60,

        )

        send_document_response = document_api.send_document(send_for_sign)

        return jsonify(send_document_response.to_dict())
