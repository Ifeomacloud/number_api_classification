from fastapi import FastAPI, HTTPException

app = FastAPI()

def is_armstrong(n: int) -> bool:
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

def get_digit_sum(n: int) -> int:
    return sum(map(int, str(n)))

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    return n > 1 and sum(i for i in range(1, n // 2 + 1) if n % i == 0) == n

# API Health Check Endpoint with Status Code 200
@app.get("/api/health-check", status_code=200)
async def health_check():
    return {"status": "API is running smoothly", "code": 200}

# Number Classification Endpoint
@app.get("/api/classify-number")
async def classify_number(number: str):
    # Handle invalid input
    if not number.isdigit():
        raise HTTPException(status_code=400, detail={"number": "alphabet", "error": True})

    number = int(number)

    # Classify properties
    properties = ["even" if number % 2 == 0 else "odd"]
    if is_armstrong(number):
        properties.append("armstrong")

    return {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": get_digit_sum(number),
        "fun_fact": f"{number} is {'an Armstrong' if is_armstrong(number) else 'not an Armstrong'} number because 3^3 + 7^3 + 1^3 = 371"
    }

# CORS setup (optional)
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
