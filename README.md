# Calculator API

A simple calculator API built with **FastAPI** in Python.  
It reuses Python functions for basic operations (add, subtract, multiply, divide) and exposes them as API endpoints.

---

## Features

- Add two numbers
- Subtract two numbers
- Multiply two numbers
- Divide two numbers (handles division by zero)
- FastAPI-powered with Swagger UI for testing

---

## Project Structure
calculator-api/
├── calculator.py # Calculator logic (functions)
├── main.py # FastAPI API endpoints
├── requirements.txt # Python dependencies
└── .gitignore # Files to ignore in Git


## Requirements
- Python 3.9+
- FastAPI
- Uvicorn

Install dependencies:

```bash
pip install -r requirements.txt

Running the API

Start the server using:

uvicorn main:app --reload


Open your browser and visit:

http://127.0.0.1:8000/docs

You’ll see Swagger UI, where you can test all API endpoints interactively.

API Endpoints
Endpoint	Method	Description	Query Params
/add	GET	Add two numbers	a, b
/subtract	GET	Subtract two numbers	a, b
/multiply	GET	Multiply two numbers	a, b
/divide	GET	Divide two numbers	a, b

Example:

GET /add?a=5&b=3
Response: { "result": 8 }

Notes

Division by zero returns a 400 error.

Calculator logic is separated into calculator.py for easy reuse and testing.

Future Improvements

Add POST endpoints to accept JSON payloads

Implement unit tests

Add authentication and authorization

Deploy to cloud (Heroku, AWS, etc.)

Author

Mounika B
GitHub: https://github.com/mounika



