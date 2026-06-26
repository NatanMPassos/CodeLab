import json
import sys
import subprocess

#find python path
python_path = sys.executable

def run_tests(code, test_cases):
    right_answers = 0
    results_dictionary = []

    #run each test case
    for case in test_cases:
        try:
            results = subprocess.run(
                [sys.executable, '-c', code],
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

        #show answer code errors (if any)
        if results.returncode != 0:
            print("Input:",case['test_input'])
            print("Answer code error:")
            print(results.stderr)
            continue

        #show input and output 
        print("Input:",case['test_input'])
        print("Expected output:",case['expected_output'].strip())
        print("Given output:", results.stdout.strip())
        
        #compare given answer with expected result
        if (results.stdout.strip() == case['expected_output'].strip()):
            print ("Correct!\n")
            right_answers += 1
            answer_check = True
        else:
            print ("Incorrect!\n")
            answer_check = False

        #return all test cases results
        results_dictionary.append({
            "input": case['test_input'],
            "expected": case['expected_output'].strip(),
            "got": results.stdout.strip(),
            "passed": answer_check
        })

    return results_dictionary

