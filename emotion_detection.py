import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, headers = headers, json = myobj)
    formatted_response = json.loads(response.text)
    emotion_scores = formatted_response["emotionPredictions"][0]["emotion"]
    scores = []
    for i, key in enumerate(emotion_scores.keys()):
        scores.append(emotion_scores[key])
    dominant = max(scores)
    rightkey = ""
    for i, key in enumerate(emotion_scores.keys()):
        if dominant == emotion_scores[key]:
            rightkey = key
    
    emotion_scores["dominant"] = rightkey
    return emotion_scores