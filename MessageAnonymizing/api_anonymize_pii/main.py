import logging
from typing import Union
from fastapi import FastAPI
from AnonymizeRequest import AnonymizeRequest
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

app = FastAPI()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

@app.get("/")
def get_request_template():
    request_template = {
        "user_question": "<raw user question: str>",
          "user_id": "<user id: str>"
          }
    return request_template

@app.post("/remove-pii/")
async def anonymize_data(request: AnonymizeRequest):
    try:
        question = request.user_question
        id = request.user_id
    except:
        return {
            "statusCode": 400,
            "message": "Request misssing a message field or a user field, an empty URL suffix for getting template "
            }
    
    anonymized_question = anonymize_pii(question)
    return {"anonymized_question": anonymized_question}


def anonymize_pii(question: str):
    analyzer = AnalyzerEngine()
    anonymizer = AnonymizerEngine()

    results = analyzer.analyze(text=question,
                               entities=get_selected_entities(),
                               language='en')
    anonymized_text = anonymizer.anonymize(text=question, analyzer_results=results)

    logger.info('Anonymizing was successful, message was forwarded')

    return anonymized_text.text


def get_selected_entities():
    return ['EMAIL_ADDRESS',
            'US_BANK_NUMBER',
            'ORGANIZATION',
            'NRP',
            'AU_ABN',
            'US_PASSPORT',
            'CREDIT_CARD',
            'DATE_TIME',
            'US_DRIVER_LICENSE',
            'IN_PAN',
            'URL',
            'PERSON',
            'SG_NRIC_FIN',
            'LOCATION',
            'IN_VEHICLE_REGISTRATION',
            'AU_MEDICARE',
            'MEDICAL_LICENSE',
            'PHONE_NUMBER',
            'US_ITIN',
            'UK_NHS',
            'CRYPTO',
            'IN_VOTER',
            'AU_TFN',
            'AU_ACN',
            'IN_PASSPORT',
            'IN_AADHAAR',
            'IBAN_CODE',
            'IP_ADDRESS',
            'US_SSN']
