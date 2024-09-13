# app.py (Backend)
from http import client

from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# Set up OpenAI API key
client = OpenAI(api_key="abbb")

# Define route to serve the HTML file
@app.route('/')
def index():
    return render_template('template.html')


# Define route to handle AI questions
@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data['question']
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": question}],)
    return jsonify({'answer': response.choices[0].text.strip()})


if __name__ == '__main__':
    app.run(debug=True)
