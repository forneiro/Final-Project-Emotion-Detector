import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyse}}

    # Make the request
    response = requests.post(url, json=myobj, headers=headers)

    
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    if response.status_code == 400:
        output['dominant_emotion'] = None
        for emotion, score in emotions.items():
            output[emotion] = None
        return emotions
    # Find the highest score
    output = {}
    max_score = -1
    for emotion, score in emotions.items():
        output[emotion] = score
        if score > max_score:
            max_score = score
            output['dominant_emotion'] = emotion

    

    return output
