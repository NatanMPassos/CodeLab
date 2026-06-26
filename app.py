from flask import Flask, request, render_template, session, redirect, url_for
from executor import run_tests
import json

#initialize flask
app = Flask(__name__)

#create session secret key
app.secret_key = 'codelab'

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file = request.files['json_file']
        exercise_list = json.load(file)
        session['exercises'] = exercise_list
        return redirect(url_for('exercise', id=1))
    else: 
        return render_template('index.html')

@app.route("/exercise/<int:id>", methods=['GET', 'POST'])
def exercise(id):
    if 'exercises' not in session:
        return redirect(url_for('home'))
    exercises_list = session['exercises']
    exercise_dictionary = next((item for item in exercises_list if item['id'] == id), None)
    if exercise_dictionary is None:
        return "Exercise not found", 404

    if request.method == 'POST':
        code = request.form['code']
        test_cases = exercise_dictionary['test_cases']
        code_results = run_tests(code, test_cases)

        if 'results_summary' not in session:
            session['results_summary'] = {}
        results_summary = session['results_summary']
        results_summary[str(id)] = all(r['passed'] for r in code_results)
        session['results_summary'] = results_summary
        session.modified = True

        return render_template(
            'exercise.html',
            exercise=exercise_dictionary,
            exercises=exercises_list,
            results = code_results,
            code=code)

    else:
        return render_template(
            'exercise.html',
            exercise=exercise_dictionary,
            exercises=exercises_list)
    
@app.route("/finish")
def finish():
    if 'exercises' not in session:
        return redirect(url_for('home'))
    exercises_list = session['exercises']
    results_summary = session.get('results_summary', {})
    return render_template(
        'finish.html',
        exercises=exercises_list,
        results_summary=results_summary)

if __name__ == "__main__":
    app.run(debug=True)

