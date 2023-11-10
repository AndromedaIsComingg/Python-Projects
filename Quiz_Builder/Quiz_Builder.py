from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quizzes.db'
db = SQLAlchemy(app)

class Quiz(db.Model):
    id = db.Column(db.String, primary_key=True)
    questions = db.Column(db.String, nullable=False)
    options = db.Column(db.String, nullable=False)
    answers = db.Column(db.String, nullable=False)


@app.route('/')
def index():
    all_quizzes = Quiz.query.all()
    quizzes = {quiz.id: {"questions": quiz.questions.split(";"), 
                         "options": quiz.options.split(";"), 
                         "answers": quiz.answers.split(";")} for quiz in all_quizzes}
    return render_template('index.html', quizzes=quizzes)

@app.route('/create', methods=['GET', 'POST'])
def create_quiz():
    if request.method == 'POST':
        quiz_id = str(uuid.uuid4())
        questions = ";".join(request.form.getlist('question'))
        options = ";".join(request.form.getlist('options'))
        answers = ";".join(request.form.getlist('answer'))
        
        new_quiz = Quiz(id=quiz_id, questions=questions, options=options, answers=answers)
        db.session.add(new_quiz)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/play/<quiz_id>', methods=['GET', 'POST'])
def play_quiz(quiz_id):
    quiz = Quiz.query.get(quiz_id)
    if quiz:
        questions_data = list(zip(quiz.questions.split(";"), quiz.options.split(";"), quiz.answers.split(";")))
        if request.method == 'POST':
            answers = [request.form.get('answer_' + str(i + 1)) for i in range(len(questions_data))]
            correct_answers = quiz.answers.split(";")
            score = sum([1 for i, j in zip(answers, correct_answers) if i == j])
            return render_template('score.html', score=score, total=len(correct_answers))
        
        return render_template('play.html', questions_data=questions_data, quiz_id=quiz_id)
    return "Quiz not found!", 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
