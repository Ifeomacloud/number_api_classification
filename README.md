# Number Classification API 
 
## This is a simple API that accepts a number and returns interesting mathematical properties along with a fun fact.

**Features**
1. Detects if a number is prime, perfect, or Armstrong.
2. Identifies whether a number is even or odd.
3. Provides the sum of digits of the number.
4. Returns a fun fact about the number.

 ## Technology Stack
1. Programming Language: Python
2. Framework: FastAPI
3. Deployment: GCP
4. Package Manager: pip

## Setup Instructions
### Prerequisites

1. Python 3.7 or higher installed.
2. pip package manager available.

## Installation
### Initialize a Git Repository:

1. git init
2. git add .
3. git commit -m "Initial commit"

### Create a GitHub Repository: Go to GitHub and create a new public repository.
Push to GitHub

1. git remote add origin (https://github.com/Ifeomacloud/number_api_classification.git)
2. git branch -M main
3. git push -u origin main

### Create and activate a virtual environment:
python -m venv venv
venv\Scripts\activate  

### Install dependencies:
pip install fastapi uvicorn requests

### Run the API
uvicorn main:app --reload
Visit http://localhost:8000/docs for interactive API documentation.

## API Endpoints
# Classify Number
GET /api/classify-number?number=<number>

Request Example
GET "http://localhost:8000/api/classify-number?number=371"

### Success Response (200)
*json*
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "class_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}

### Error Response (400)
json
{
    "number": "alphabet",
    "error": true
}

### Development Notes
1. I ensured that CORS is handled appropriately.
2. Thoroughly tested the API for edge cases (negative numbers, invalid inputs, etc.).
3. Response times is  < 500ms.
