import requests
import json

def emotion_detector(text_to_analyse):
    # URL of the sentiment analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    input_json = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID for the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=input_json, headers=header)

    # returning the response text property 
    # return response.text 

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extracting sentiment label and score from the response
    # label = formatted_response['documentSentiment']['label']
    # score = formatted_response['documentSentiment']['score']
    anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
    dominant_emotion = anger
    dominant_emotion_name = 'anger'

    disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    if (disgust > dominant_emotion):
        dominant_emotion = disgust
        dominant_emotion_name = 'disgust'

    fear    = formatted_response['emotionPredictions'][0]['emotion']['fear']
    if (fear > dominant_emotion):
        dominant_emotion = fear
        dominant_emotion_name = 'fear'

    joy     = formatted_response['emotionPredictions'][0]['emotion']['joy']
    if (joy > dominant_emotion):
        dominant_emotion = joy
        dominant_emotion_name = 'joy'

    sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    if (sadness > dominant_emotion):
        dominant_emotion = sadness
        dominant_emotion_name = 'sadness'

    
    #dominant_emotion= formatted_response['documentSentiment']['dominant_emotion']



    # Returning a dictionary containing sentiment analysis results
    # return {'label': label, 'score': score}
    return {
        'anger': anger, 
        'disgust': disgust, 
        'fear': fear, 
        'joy': joy, 
        'sadness': sadness,
        'dominant_emotion': dominant_emotion_name
    }