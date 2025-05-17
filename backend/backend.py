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

# {tasks :
#       task:
#             task_name:
#             priority:
#             effort: }



@app.route('/analyze', methods=['POST'])
def analyze():
    tasks = request.get_json()
    print(tasks)
    prompt = f"Given the following list of tasks in a JSON format, rank them in terms of priority and output it in JSON format: {tasks}"
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=150,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )
    # prompt prioritized_list into gpt and ask it to create a schedule from it
    prioritized_list = response.choices[0].message.content
    data = []
    prompt = {
        "data": data
    }
    return jsonify(lol)


if __name__ == '__main__':
    app.run(debug=True)