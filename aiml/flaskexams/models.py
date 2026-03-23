from flaskexams import db

class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)

class Answers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set_oprabation'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)