from flask import Flask, request
import requests

API_URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADER = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze):
    input_data = { "raw_document": { "text": text_to_analyze } }
    resp = requests.post(API_URL,
        headers=HEADER,
        json=input_data)

    data = resp.json()
    print(data)
    