from flask import Flask, request, json
import requests

API_URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADER = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze):
    input_data = { "raw_document": { "text": text_to_analyze } }
    resp = requests.post(API_URL,
        headers=HEADER,
        json=input_data)

    data = resp.json()
    emotion_data = data["emotionPredictions"][0]["emotion"]

    emotion = None
    rating = None

    for x, y in emotion_data.items():
        if emotion is None:
            emotion = x
            rating = y
            continue
        
        if y > rating:
            rating = y
            emotion = x

    emotion_data["dominant_emotion"] = emotion
   
    print(emotion_data)

   