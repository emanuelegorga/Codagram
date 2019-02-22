import os
import config
from flask import Flask, render_template, request, jsonify, flash, Markup
from multiprocessing import Value
# from lib import generator
from sqlalchemy.event import listen
from sqlalchemy import event, DDL
from flask_sqlalchemy import SQLAlchemy

counter = Value('i', 1)
app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import *

@app.before_first_request
def setup():
    # ques = Question.query.filter_by(id=1).delete()
    db.session.query(Question).delete()
    db.session.execute("ALTER SEQUENCE questions_id_seq RESTART WITH 1;")
    db.session.commit()
    db.session.add(Question(question=u'q1 question', choice1=u'q1 choice1', choice2=u'q1 choice2', choice3=u'q1 choice3', choice4=u'q1 choice4', answer=u'q1 choice1'))
    db.session.add(Question(question=u'q2 question', choice1=u'q2 choice1', choice2=u'q2 choice2', choice3=u'q2 choice3', choice4=u'q2 choice4', answer=u'q2 choice2'))
    db.session.add(Question(question=u'q3 question', choice1=u'q3 choice1', choice2=u'q3 choice2', choice3=u'q3 choice3', choice4=u'q3 choice4', answer=u'q3 choice3'))
    db.session.commit()
    db.session.execute("INSERT INTO questions(question, choice1, choice2, choice3, choice4, answer) VALUES('q4 question', 'q4 choice1', 'q4 choice2', 'q4 choice3', 'q4 choice4', 'q4 choice4');")
    db.session.commit()

@app.route("/")
def root():
    return "Index page - currently empty"

@app.route("/landing")
def landing():
    return "Welcome to our landing page :-)."
    # return render_template('question.html')

@app.route("/getallquestions")
def get_all():
    try:
        questions=Question.query.all()
        return jsonify([q.serialize() for q in questions])
    except Exception as q:
	    return(str(q))

@app.route("/question/<id_>", methods=['GET', 'POST'])
def get_question_by_id(id_):

    question = Question.query.filter_by(id=id_).first()

    if request.method =='POST':
        # return "in the post request method"
        print(request.form['question'])
        if request.form['question'] == question.answer:
            print("Correct Well done")
            with counter.get_lock():
                counter.value += 1
                id = counter.value
                # id = str(unique_count)
                # print(id)
            # return "Correct Well done!"
            button = Markup(f'<form method="GET" action="/question/{id}"><button type="submit">next</button></form>')
            flash(button)
            return render_template('question.html',question=question)
        else:
            # print("Wrong! Try Again")
            # return "Wrong! Try Again"
            flash('this is a test flash message')
            return render_template('question.html',question=question)

    return render_template('question.html',question=question)

# @app.route("/question", methods=['GET', 'POST'])
# def get_question():
#     if request.method =='POST':
#         # return "string one"
#
#         print(request.form['question'])
#         if request.form['question'] == 'correct_answer':
#             # print("Correct Well done")
#             return "Correct Well done!"
#         else:
#             # print("Wrong! Try Again")
#             return "Wrong! Try Again"
#
#     # question = questions.generate_question()
#     return render_template('question.html',question=question)

if __name__ == '__main__':
    app.run()
