from flask import Flask, request
from executor import run_tests
import json

#initialize flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>hello world</h1>"

@app.route("/exercise/<int:id>", methods=['GET', 'POST'])
def exercise(id):
    with open('exercises.json', 'r', encoding='utf-8') as file:
        exercises_list = json.load(file)
    exercise_dictionary = next((item for item in exercises_list if item['id'] == id), None)
    if exercise_dictionary is None:
        return "Exercise not found", 404

    if request.method == 'POST':
        code = request.form['code']
        test_cases = exercise_dictionary['test_cases']
        results = run_tests(code, test_cases)
        return str(results)

    else:
        return f"""
        <h2>{exercise_dictionary['exercise']}</h2>
        <form method="POST">
            <textarea name="code"></textarea>
            <button type="submit">Submit</button>
        </form>
        """

if __name__ == "__main__":
    app.run(debug=True)

