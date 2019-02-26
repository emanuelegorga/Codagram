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

@app.route("/")
def root():
    return render_template('index.html')

@app.route("/introduction")
def introduction():
    return render_template('introduction.html')

@app.route("/getallquestions")
def get_all():
    try:
        questions=Question.query.all()
        return jsonify([q.serialize() for q in questions])
    except Exception as q:
	    return(str(q))

@app.route("/tutorial/<language>")
def tutorial_ruby(language):
    if language == 'ruby':
        return render_template('tutorialruby.html')
    elif language == 'python':
        return render_template('tutorialpython.html')
    elif language == 'javascript':
        return render_template('tutorialjavascript.html')
    else:
        return 'Error'

@app.route("/question/<id_>", methods=['GET', 'POST'])
def get_question_by_id(id_):

    question = Question.query.filter_by(id=id_).first()

    if request.method =='POST':
        # print(request.form['question'])
        if request.form['question'] == question.answer:
            with counter.get_lock():
                counter.value += 1
                id = counter.value
            button = Markup(f'<form method="GET" action="/question/{id}"><button type="submit">next</button></form>')
            flash("Well done!")
            flash(button)
            return render_template('question.html',question=question)
        else:
            flash('That is wrong. Try again!')
            return render_template('question.html',question=question)

    return render_template('question.html',question=question)

@app.route("/questionlevel2_ruby/<id_>", methods=['GET', 'POST'])
def get_questionlevel2_by_id(id_):

    question2 = QuestionLevel2.query.filter_by(id=id_).first()
    if request.method =='POST':
        # print(request.form['user_answer'])
        if request.form['user_answer'] == question2.answer:
            with counter_questionlevel2.get_lock():
                counter_questionlevel2.value += 1
                id = counter_questionlevel2.value
            button = Markup(f'<form method="GET" action="/questionlevel2_ruby/{id}"><button type="submit">next</button></form>')
            flash("Well done!")
            flash(button)
            return render_template('question2.html',question2=question2)
        else:
            flash('That is wrong. Try again!')
            return render_template('question2.html',question2=question2)

    return render_template('question2.html',question2=question2)

@app.before_first_request
def setup():
    db.session.query(Question).delete()
    db.session.execute("ALTER SEQUENCE questions_id_seq RESTART WITH 1;")
    db.session.commit()
# ------------ RUBY QUESTIONS PART 1 ------------
    db.session.add(Question(question=u'1) How many data types are available in Ruby?', choice1=u'1', choice2=u'2', choice3=u'3', choice4=u'4', answer=u'3'))
    db.session.add(Question(question=u'2) Which of the following is a correct way to define a string?', choice1=u'"Hello"', choice2=u'Hello', choice3=u'-Hello-', choice4=u'(Hello)', answer=u'"Hello"'))
    db.session.add(Question(question=u'3) Which of the following is known as a boolean value?', choice1=u'Yes', choice2=u'Truth', choice3=u'Real', choice4=u'True', answer=u'True'))
    db.session.add(Question(question=u'4) How do you display "Hi there!" on the screen?', choice1=u'put "Hi there!"', choice2=u'puts "Hi there!"', choice3=u'"puts Hi there!"', choice4=u'puts Hi there!', answer=u'puts "Hi there!"'))
    db.session.add(Question(question=u'5) How do you display the number 23 on the screen?', choice1=u'23', choice2=u'puts 23', choice3=u'23 puts', choice4=u'puts "23"', answer=u'puts 23'))
    db.session.add(Question(question=u'6) Which of the following is a correct way to assign the number 30 to the variable a?', choice1=u'a = 30', choice2=u'a(30)', choice3=u'30 = a', choice4=u'a == 30', answer=u'a = 30'))
    db.session.add(Question(question=u'7) Given a variable a = 25, how do you display the value of the variable "a"?', choice1=u'puts "a"', choice2=u'puts variable(a)', choice3=u'puts a', choice4=u'a', answer=u'puts a'))
    db.session.add(Question(question=u'8) Which of the following is not a valid datatype in Ruby?', choice1=u'Integer', choice2=u'String', choice3=u'Timedate', choice4=u'Boolean', answer=u'Timedate'))
    db.session.add(Question(question=u'9) What is the extension used for saving the ruby file?', choice1=u'.ruby', choice2=u'.r', choice3=u'.rb', choice4=u'.ry', answer=u'.rb'))
    db.session.add(Question(question=u'10) What do you use to comment out a single line of code in Ruby?', choice1=u'#', choice2=u'begin and end', choice3=u'//', choice4=u'<!- ->', answer=u'#'))
# ------------ RUBY QUESTIONS PART 2 ------------
    db.session.commit()

    db.session.query(QuestionLevel2).delete()
    db.session.execute("ALTER SEQUENCE questions_level2_id_seq RESTART WITH 1;")
    db.session.commit()
    db.session.add(QuestionLevel2(language=u'Ruby', question_display_id=1, question=u'1) What do you use in between an object and a method?', answer=u'.'))
    db.session.add(QuestionLevel2(language=u'Ruby', question_display_id=2, question=u'2) What is 8 % 5', answer=u'3'))
    db.session.add(QuestionLevel2(language=u'Ruby', question_display_id=3, question=u'3) Given the string "World" how do you add Hello in front of?', answer=u'"#{Hello} World"'))
    db.session.add(QuestionLevel2(language=u'Ruby', question_display_id=4, question=u'4) What must every class have?', answer=u'end'))
    db.session.add(QuestionLevel2(language=u'Ruby', question_display_id=5, question=u'5) How would you display the number 42 as a string?', answer=u'puts "42"'))
    db.session.add(QuestionLevel2(language=u'Ruby', question_display_id=6, question=u'6) Given an array a = [25, "Yikes!", false]. What would print a[2] output?', answer=u'false'))
    db.session.add(QuestionLevel2(language=u'Ruby', question_display_id=7, question=u'7) Given an array a = [25, "Yikes!", false]. If you do a.push["WOW"], what would print a[3] output?', answer=u'WOW'))
    db.session.add(QuestionLevel2(language=u'Ruby', question_display_id=8, question=u'8) Given a hash h = ["one" => "un", "two" => "deux", "three" => "trois"]. What would the output be if you write h[2]', answer=u'trois'))
    db.session.add(QuestionLevel2(language=u'Ruby', question_display_id=9, question=u'9) Given a string s = "Test123". What would s.reverse.upcase output?', answer=u'321TSET'))
    db.session.add(QuestionLevel2(language=u'Ruby', question_display_id=9, question=u'10) Given a string s = "Test123". What would s.include?("est1") output?', answer=u'true'))

    db.session.add(QuestionLevel2(language=u'Python', question_display_id=0, question=u'q1 What is a Python?', answer=u'Snake'))
    db.session.commit()


if __name__ == '__main__':
    app.run()
