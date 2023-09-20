from flask import Flask, request, jsonify, Response
import nltk

# Downloading before importing SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)

@app.route('/')
def index():
    with open('index.html', 'r', encoding='utf-8') as f:
        return Response(f.read(), content_type='text/html; charset=utf-8')

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    try:
        print("Received data: ", request.json)
        text = request.json.get('text', '')
        sia = SentimentIntensityAnalyzer()
        score = sia.polarity_scores(text)
        print("Sentiment score: ", score)
        return jsonify(score)
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "An error occurred"}), 500

@app.route('/ask', methods=['POST'])
def ask_question():
    question = request.json.get('question', '')
    answer = "Your answer to the question: " + question
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
