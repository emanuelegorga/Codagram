from app import db

class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String())
    choice1 = db.Column(db.String())
    choice2 = db.Column(db.String())
    choice3 = db.Column(db.String())
    choice4 = db.Column(db.String())
    answer = db.Column(db.String())

    def __init__(self, question, choice1, choice2, choice3, choice4, answer):
        self.question = question
        self.choice1 = choice1
        self.choice2 = choice2
        self.choice3 = choice3
        self.choice4 = choice4
        self.answer = answer

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'question': self.question,
            'choice1': self.choice1,
            'choice2': self.choice2,
            'choice3': self.choice3,
            'choice4': self.choice4,
            'answer': self.answer
        }
