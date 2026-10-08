from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detect_emotion():
    text = request.args.get("textToAnalyze")

    if text is None:
        return {"message": "Missing parameter 'text'"}, 404

    data = emotion_detector(text)
    
    if data["dominant_emotion"] == "None":
        output = "<b>Invalid text! Please try again!</b>"
    else:
        output = f"For the given statement, the system response is 'anger': {data['anger']}, 'disgust': {data['disgust']}, 'fear': {data['fear']}, 'joy': {data['joy']}, and 'sadness': {data['sadness']}. The dominant emotion is <b>{data['dominant_emotion']}</b>"
    
    return output

@app.route("/")
def root():
    return render_template('index.html')    
