"""
This module implements a Flask web application for emotion detection.
It serves a web page and processes text input using an emotion detection API.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """
    Renders the index page for the emotion detector web application.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emot_detection():
    """
    Handles the /emotionDetector route by accepting text input via query parameters,
    processes it using the emotion_detector function, and returns the result.
    If the dominant emotion is None, returns an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    # If dominant_emotion is None, return an error message
    if response.get('dominant_emotion') is None:
        return "Invalid text! Please try again!"
    # Otherwise, return the valid emotions and dominant emotion
    return (f"For the given statement, the system's response is "
            f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
            f"'fear': {response['fear']}, 'joy': {response['joy']}, "
            f"'sadness': {response['sadness']}. "
            f"The dominant emotion is {response['dominant_emotion']}.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
