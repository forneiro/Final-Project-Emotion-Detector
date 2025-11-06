from flask import Flask, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    # Response
    response = requests.post(url, json=myobj, headers=header)
    # Formatted response in json
    formatted_response = json.loads(response.text)
    
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    # Initialiaze an empty object
    output = {}
    dominant_emotion = 0
    # Add emotions to output object
    for emotion in emotions:
        # If condition to find the highest score
        if (emotions[emotion] > dominant_emotion):
            dominant_emotion = emotions[emotion]
            output['dominant_emotion'] = emotion
        output[emotion] = emotions[emotion]
    
    return output
