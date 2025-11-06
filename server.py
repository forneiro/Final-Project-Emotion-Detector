'''
This is the server
'''
from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetecor')
def sent_analyzer():
    '''
    Retrieve de requests and sent and response
    '''
    text_to_analyse = request.args.get('text_to_analyse')
    if not text_to_analyse:
        return jsonify({"error": "You must provide a 'text_to_analyse' parameter"}), 400
    response = emotion_detector(text_to_analyse)
    if response.get('dominant_emotion') is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400
    return jsonify(response)

@app.route("/")
def render_index_page():
    ''' This code render the page
    '''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8070)
