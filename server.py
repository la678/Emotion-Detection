""" Defining server.py """
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector


app=Flask("__name__")

@app.route("/")
def render_index():
    """Render the index page."""
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detection():
    """Detect emotion based on the given text."""
    # if request.method == 'POST':
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    if result['dominant_emotion'] is None:
        # Handle case where dominant_emotion is None
        return "Invalid text! Please try again!"
    response_data = {
        "anger": result['anger'],
        "disgust": result['disgust'],
        "fear": result['fear'],
        "joy": result['joy'],
        "sadness": result['sadness'],
        "dominant_emotion": result.get('dominant_emotion', 'unknown'),
    }

    return (
        f"For the given statement, the system response is 'anger': {response_data['anger']},"
        f"'disgust': {response_data['disgust']}, 'fear': {response_data['fear']}, 'joy': "
        f"{response_data['joy']} and 'sadness': {response_data['sadness']}. The dominant emotion" 
        f" is {response_data['dominant_emotion']}"
    )

if __name__ == "__main__" :
    app.run(debug=True, port=5000)
