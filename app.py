import os
import config
from flask import Flask, render_template, request
from lib import generator
from lib import questions
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route("/")
def root():
    return "Index page - currently empty"
# def generate_buzz():
#     page = '<html><body><h1>'
#     page += generator.generate_buzz()
#     page += '</h1></body></html>'
#     return page

@app.route("/landing")
def landing():
    return "Welcome to our landing page :-)."
    # return render_template('question.html')

@app.route("/question", methods=['GET', 'POST'])
def get_question():
    if request.method =='POST':
        # return "string one"

        print(request.form['question'])
        if request.form['question'] == 'correct_answer':
            # print("Correct Well done")
            return "Correct Well done!"
        else:
            # print("Wrong! Try Again")
            return "Wrong! Try Again"

    question = questions.generate_question()
    return render_template('question.html',question=question)
