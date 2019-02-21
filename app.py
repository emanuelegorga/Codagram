import os
import config
from flask import Flask, render_template, request
from lib import generator
from sqlalchemy.event import listen
from sqlalchemy import event, DDL
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import *

@app.before_first_request
def setup():
    db.session.add(Question(question=u'q1 question1', choice1=u'q1 choice1', choice2=u'q1 choice2', choice3=u'q1 choice3', choice4=u'q1 choice4', answer=u'q1 choice1'))
    db.session.add(Question(question=u'q2 question1', choice1=u'q2 choice1', choice2=u'q2 choice2', choice3=u'q2 choice3', choice4=u'q2 choice4', answer=u'q2 choice2'))
    db.session.add(Question(question=u'q3 question1', choice1=u'q3 choice1', choice2=u'q3 choice2', choice3=u'q3 choice3', choice4=u'q3 choice4', answer=u'q3 choice3'))
    db.session.commit()

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

    # question = questions.generate_question()
    return render_template('question.html',question=question)

if __name__ == '__main__':
    app.run()
