'''
Application in Flask used for emotion detection
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    '''
    This function is used to call application
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        response_text = "Invalid Input! Please try again."
    else:
        response_text = f"For the given statement, the system response is 'anger': \
                    {response['anger']}, 'disgust': {response['disgust']}, \
                    'fear': {response['fear']}, 'joy': {response['joy']}, \
                    'sadness': {response['sadness']}. The dominant emotion is \
                    {response['dominant emotion']}."

    return response_text

@app.route("/")
def render_index_page():
    '''
    This function is used to render the html interface
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
