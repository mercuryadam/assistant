from flask import Flask, request
app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask_question():
    question = request.json['question']
    # Your Python program logic here
    return "Your answer"

if __name__ == '__main__':
    app.run(debug=True)
