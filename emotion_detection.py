import requests
import json

def sentiment_analyzer(text_to_analyse):
    # URL of the sentiment analysis service
    url = ''

    # Constructing the request payload in the expected format
    input_json = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID for the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=input_json, headers=header)

    # returning the respinse text property 
    # return response.text 

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extracting sentiment label and score from the response
    label = formatted_response['documentSentiment']['label']
    score = formatted_response['documentSentiment']['score']

    # Returning a dictionary containing sentiment analysis results
    return {'label': label, 'score': score}