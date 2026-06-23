import json
import sys
import subprocess

#find python path
python_path = sys.executable

#open json
with open('exercises.json', 'r', encoding='utf-8') as file:
    exercise_list = json.load(file)

#separate json 
exercise = exercise_list[0]['exercise']
case_list = exercise_list[0]['test_cases']

right_answers = 0
total_cases = len(case_list)

#run each test case
for case in case_list:
    try:
        results = subprocess.run(
            [sys.executable, 'other_code.py'],
            input= case['test_input'],
            capture_output=True, 
            text=True,
            encoding='cp1252',
            timeout=5
        )
    #timeout treatment
    except subprocess.TimeoutExpired:
        print("Input:",case['test_input'])
        print("Timeout error: answer code took too long to run.\n")
        continue
        
    #showing answer code errors (if any)
    if results.returncode != 0:
        print("Input:",case['test_input'])
        print("Answer code error:")
        print(results.stderr)
        continue

    print("Input:",case['test_input'])
    print("Expected output:",case['expected_output'].strip())
    print("Given output:", results.stdout.strip())
    
    #compare given answer with expected result
    if (results.stdout.strip() == case['expected_output'].strip()):
        print ("Correct!\n")
        right_answers += 1
    else:
        print ("Incorrect!\n")

print(f"You got {right_answers} out of {total_cases} cases right!")
