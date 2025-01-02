from flask import Flask, request, jsonify, render_template
from models.emotion_model import analyze_emotion

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# API route to handle chatbot responses
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')
    if not user_input:
        return jsonify({'response': "I'm here to listen. Please tell me more."})

    emotion, confidence = analyze_emotion(user_input)
    response = generate_response(emotion)

    return jsonify({'response': response, 'emotion': emotion, 'confidence': confidence})

def generate_response(emotion):
    responses = {
        "happy": "That's wonderful! Keep up the positivity!",
        "sad": "I'm sorry you're feeling this way. Take a deep breath; you are not alone.",
        "angry": "It’s okay to feel angry sometimes. Let’s work through this together.",
        "neutral": "I’m here for you. How can I help?",
    }
    return responses.get(emotion, "I'm here to listen. Please tell me more.")

if __name__ == '__main__':
    app.run(debug=True)
