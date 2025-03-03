# API key

fileopen = open("Database\\Api.txt","r")
API = fileopen.read()
fileopen.close()


import openai
from dotenv import load_dotenv

from flask import Flask, render_template, request, jsonify


openai.api_key = API 
load_dotenv()
completion = openai.Completion()

app = Flask(__name__)

def QuestionsAnswer(question, chat_log = None):
    FileLog = open("Database\\TEDBot.txt","r")
    chat_log_template = FileLog.read()
    FileLog.close()

    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log}Question : {question}\nAnswer : '
    response = completion.create(   
        model = "text-davinci-002",
        prompt=prompt,
        temperature = 0,
        max_tokens = 100,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0)
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nQuestion : {question} \nAnswer : {answer}"
    FileLog = open("Database\\TEDBot.txt","w")
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return answer

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        question = request.form.get('msgs')
        answer = QuestionsAnswer(question)
        return answer

    return render_template('TEDBot.html')

if __name__ == '__main__':
    app.run(debug=True)
