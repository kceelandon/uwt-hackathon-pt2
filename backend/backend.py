from flask import Flask # type: ignore
from flask import jsonify, request  # type: ignore
from os import environ
from openai import OpenAI # type: ignore
from dotenv import load_dotenv # type: ignore
from flask_cors import CORS # type: ignore
import re

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
    
    prompt = f"Given the following list of tasks in a JSON format,  table format: {tasks} assume work is normal working hours please give me a time schedule please create a tenaitve scehdile that will allow me to optimize energy to get all task done. please please please dont giver mer any other words please jsut give me tthe schdule formated like the following | 6:30 AM - 7:00 AM | Wake up & Morning routine | seperate each event by a space and comma"
    print(prompt)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=150,
        messages=[
            {"role": "system", "content": "You are a helpful assistant managing youre supervisors schedule."},
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )
    # prompt prioritized_list into gpt and ask it to create a schedule from it
    prioritized_list = response.choices[0].message.content
    print(prioritized_list)
    prompt = {
        "data":"lol"
    }
    
    return jsonify(prompt)


if __name__ == '__main__':
    app.run(debug=True)

  