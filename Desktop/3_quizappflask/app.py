from flask import Flask, render_template, request, redirect, url_for

#templatepath
app = Flask(__name__, template_folder='templates')

# questions
questions = [
    {
        'question': '1. What is the capital of France?',
        'options': ['Paris', 'London', 'Berlin', 'Rome'],
        'correct_answer': 'Paris'
    },
    {
        'question': '2. What does HTML stand for?',
        'options': ['Hyper Text Markup Language', 'Hyperlinks and Text Markup Language', "Home Tool Markup Language", "Hyper Tools Markup Language"],
        "correct_answer": 'Hyper Text Markup Language'
    },
    {
        'question': "3. Which of the following is not a valid data type in Python?",
        "options": ["int", "float", "decimal", "bool"],
        "correct_answer": 'decimal'
    },
    {
        'question': "4. What is output of... print('hello'[::-1]) ?",
        'options': ["hello", "olleh", "llohe", "ollhe"],
        "correct_answer": 'olleh'
    },
    {
        'question': "5. What does the 'range()' function return?",
        'options': ["A list of integers", "A generator object", "A dictionary", "A string"],
        "correct_answer": "A list of integers"
    }
]

#index
@app.route('/')
def index():
    return render_template('index.html', questions=questions)

#result
@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    user_answers = request.form
    for question in questions:
        if user_answers.get(question['question']) == question['correct_answer']:
            score += 1
    percentage_score = (score / len(questions)) * 100
    return render_template('result.html', score=score, total_questions=len(questions), percentage_score=percentage_score )

if __name__ == '__main__':
    app.run(debug=True)
