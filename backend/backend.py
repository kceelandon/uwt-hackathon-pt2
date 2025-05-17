from flask import Flask # type: ignore
from flask import jsonify, request  # type: ignore
from os import environ
from openai import OpenAI # type: ignore
from dotenv import load_dotenv # type: ignore
from flask_cors import CORS # type: ignore

app = Flask(__name__)
CORS(app)

load_dotenv()

OPENAI_API_KEY = environ["OPENAI_API_KEY"]

client = OpenAI()
@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data.get("text", "")
    length = len(text)
    return jsonify({"length": length, "original": text})

if __name__ == '__main__':
    app.run(debug=True)