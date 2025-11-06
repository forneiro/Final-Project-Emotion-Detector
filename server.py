from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetection')
def sent_analyzer():
    textToAnalyse = request.args.get('text_to_analyse')
    
    if not textToAnalyse:
        return jsonify({"error": "You must provide a 'text_to_analyse' parameter"}), 400
    
    response = emotion_detector(textToAnalyse)
    return jsonify(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8010)
