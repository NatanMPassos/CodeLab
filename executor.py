import sys
import subprocess

def run_tests(code, test_cases):
    results_dictionary = []
    for case in test_cases:
        try:
            results = subprocess.run(
                [sys.executable, '-c', code],
                input=case['test_input'],
                capture_output=True,
                text=True,
                encoding='cp1252',
                timeout=5
            )
        except subprocess.TimeoutExpired:
            results_dictionary.append({
                "input": case['test_input'],
                "expected": case['expected_output'],
                "got": "Timeout",
                "passed": False
            })
            continue

        if results.returncode != 0:
            results_dictionary.append({
                "input": case['test_input'],
                "expected": case['expected_output'],
                "got": "Error: " + results.stderr.strip(),
                "passed": False
            })
            continue

        answer_check = results.stdout.strip() == case['expected_output'].strip()
        results_dictionary.append({
            "input": case['test_input'],
            "expected": case['expected_output'].strip(),
            "got": results.stdout.strip(),
            "passed": answer_check
        })
    return results_dictionary