"""
This module contains a Flask web application for an Emotion Detector.

The application has two routes:
    - /emotionDetector: accepts a text to analyze as a request argument and
                        returns the sentiment analysis results as a string.
    - /: renders an HTML template for the user to input text and submit for
          analysis.

The application calls the emotion_detector function from the EmotionDetection
module to perform the sentiment analysis.

The application is configured to run on host 0.0.0.0 and port 5000.
"""

from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def call_emotion_detector():
    """
    Accepts a text to analyze as a request argument and returns the sentiment
    analysis results as a string.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    # Extract the anger and score from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    # Return a formatted string with the sentiment label and score
    if dominant_emotion is None :
        return " Invalid text! Please try again"
    return f"For the given statement, the system response is anger: {anger}, disgust: {disgust},\
         fear:  {fear}, joy: {joy}, sadness: {sadness} . \
         The dominant emotion is {dominant_emotion}"



@app.route("/")
def render_index_page():
    """
    Renders an HTML template for the user to input text and submit for analysis.
    """
    return render_template('index.html')



if __name__ == "__main__":
    app.run( host = "0.0.0.0", port = 5000)
