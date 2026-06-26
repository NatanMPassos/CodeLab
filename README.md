# CodeLab

A lightweight web platform for Python coding exercises with automatic test case validation.
This project is a Work In Progress, features still pending:
-Code will not be lost when switching between exercises
-json file format check
-Several visual upgrades

## Overview

CodeLab allows users to upload a JSON file with Python exercises, write solutions in a browser based code editor, and receive instant feedback through automatic test case execution.

## Notable Features

- JSON based exercise loading
- In browser Python code editor with syntax highlighting (CodeMirror)
- Automatic test case validation via subprocess execution
- Timeout protection against infinite loops
- Per exercise results with input, expected output, and actual output
- Final summary screen showing overall performance

## Exercise JSON Format

```json
[
  {
    "id": 1,
    "exercise": "Given a number N, print the square of N",
    "test_cases": [
      {"test_input": "5", "expected_output": "25"},
      {"test_input": "3", "expected_output": "9"}
    ]
  },
  {
    "id": 2,
    "exercise": "Given a number N, print the cube of N",
    "test_cases": [
      {"test_input": "5", "expected_output": "125"},
      {"test_input": "3", "expected_output": "27"}
    ]
  }
]
```
A working JSON file is included in the repository

## Getting Started

1. Clone the repository
```bash
git clone https://github.com/NatanMPassos/CodeLab
cd CodeLab
```

2. Install dependencies
```bash
pip install flask
```

3. Run the application
```bash
python app.py
```

4. Open in browser
```
http://localhost:5000
```

## Tech Stack

- Backend: Python, Flask, Python subprocess
- Frontend: HTML, Jinja2, CodeMirror
