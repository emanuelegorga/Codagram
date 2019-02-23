import os
import config
from flask import Flask, render_template, request, jsonify, flash, Markup
from multiprocessing import Value
from sqlalchemy.event import listen
from sqlalchemy import event, DDL
from flask_sqlalchemy import SQLAlchemy

counter = Value('i', 1)
counter_questionlevel2 = Value('i', 1)
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
    db.session.execute("INSERT INTO questions(question, choice1, choice2, choice3, choice4, answer) \
                        VALUES ('q4 question', 'q4 choice1', 'q4 choice2', 'q4 choice3', 'q4 choice4', 'q4 choice4');"
                        )
    db.session.commit()

    db.session.query(QuestionLevel2).delete()
    db.session.execute("ALTER SEQUENCE questions_level2_id_seq RESTART WITH 1;")
    db.session.commit()
    db.session.add(QuestionLevel2(language=u'Ruby', question_display_id=1, question=u'q1 Which bootcamp are you currently studying at?', answer=u'Makers Academy'))
    db.session.add(QuestionLevel2(language=u'Ruby', question_display_id=2, question=u'q2 Name of your cohort?', answer=u'November 2018'))
    db.session.add(QuestionLevel2(language=u'Python', question_display_id=1, question=u'q1 What is a Python?', answer=u'Snake'))
    db.session.commit()


@app.route("/")
def root():
    # return "Index page - currently empty"
    return render_template('index.html')

@app.route("/introduction")
def introduction():
    # return "Welcome to our landing page :-)."
    return render_template('introduction.html')

@app.route("/getallquestions")
def get_all():
    try:
        questions=Question.query.all()
        return jsonify([q.serialize() for q in questions])
    except Exception as q:
	    return(str(q))

@app.route("/tutorial_ruby")
def tutorial_ruby():
    # return "Welcome to our landing page :-)."
    return render_template('tutorialruby.html')

@app.route("/tutorial_python")
def tutorial_python():
    # return "Welcome to our landing page :-)."
    return render_template('tutorialpython.html')

@app.route("/tutorial_javascript")
def tutorial_javascript():
    # return "Welcome to our landing page :-)."
    return render_template('tutorialjavascript.html')

@app.route("/question_ruby/<id_>", methods=['GET', 'POST'])
def get_question_by_id(id_):

    question = Question.query.filter_by(id=id_).first()

    if request.method =='POST':
        print(request.form['question'])
        if request.form['question'] == question.answer:
            print("Correct Well done")
            with counter.get_lock():
                counter.value += 1
                id = counter.value
            button = Markup(f'<form method="GET" action="/question_ruby/{id}"><button type="submit">next</button></form>')
            flash(button)
            return render_template('question.html',question=question)
        else:
            flash('this is a test flash message')
            return render_template('question.html',question=question)

    return render_template('question.html',question=question)

@app.route("/questionlevel2_ruby/<id_>", methods=['GET', 'POST'])
def get_questionlevel2_by_id(id_):

    question2 = QuestionLevel2.query.filter_by(id=id_).first()
    # print('question2')
    # print(question2)
    if request.method =='POST':
        print(request.form['user_answer'])
        if request.form['user_answer'] == question2.answer:
            # print("Correct Well done")
            with counter_questionlevel2.get_lock():
                counter_questionlevel2.value += 1
                id = counter_questionlevel2.value
            button = Markup(f'<form method="GET" action="/questionlevel2_ruby/{id}"><button type="submit">next</button></form>')
            flash(button)
            return render_template('question2.html',question2=question2)
        else:
            flash('this is a flash message to feedback to user the answer is wrong!')
            return render_template('question2.html',question2=question2)

    return render_template('question2.html',question2=question2)

if __name__ == '__main__':
    app.run()
