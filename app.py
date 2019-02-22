import os
import config
from flask import Flask, render_template, request, jsonify, flash, Markup
from multiprocessing import Value
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
        print(request.form['question'])
        if request.form['question'] == question.answer:
            print("Correct Well done")
            with counter.get_lock():
                counter.value += 1
                id = counter.value
            button = Markup(f'<form method="GET" action="/question/{id}"><button type="submit">next</button></form>')
            flash(button)
            return render_template('question.html',question=question)
        else:
            flash('this is a test flash message')
            return render_template('question.html',question=question)

    return render_template('question.html',question=question)

if __name__ == '__main__':
    app.run()
