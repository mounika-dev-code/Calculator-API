from fastapi import FastAPI, HTTPException
import calculator

app = FastAPI(title="Calculator API")
@app.get("/add")
def add_numbers(a: float, b: float):
    return {"result": calculator.add(a, b)}

@app.get("/subtract")
def subtract_numbers(a: float, b: float):
    return {"result": calculator.subtract(a, b)}

@app.get("/multiply")
def multiply_numbers(a: float, b: float):
    return {"result": calculator.multiply(a, b)}

@app.get("/divide")
def divide_numbers(a: float, b: float):
    try:
        result = calculator.divide(a, b)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
