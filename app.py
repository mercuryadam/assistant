from flask import Flask, request
app = Flask(__name__)

import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize the VADER sentiment intensity analyzer
sia = SentimentIntensityAnalyzer()

# Sample text
sample_text1 = "I love this product! It's amazing."
sample_text2 = "This is terrible, I hate it."

# Get the sentiment score
score1 = sia.polarity_scores(sample_text1)
score2 = sia.polarity_scores(sample_text2)

# Interpret the score
def interpret_score(score):
    compound = score['compound']
    if compound >= 0.05:
        return "Positive"
    elif compound <= -0.05:
        return "Negative"
    else:
        return "Neutral"

print(f"Sentiment of text 1: {interpret_score(score1)}")
print(f"Sentiment of text 2: {interpret_score(score2)}")

@app.route('/ask', methods=['POST'])
def ask_question():
    question = request.json['question']
    # Your Python program logic here
    return print("Your answer")

if __name__ == '__main__':
    app.run(debug=True)
