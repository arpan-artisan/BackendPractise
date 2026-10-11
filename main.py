from fastapi import FastAPI, HTTPException
import time
import asyncio

app = FastAPI()

@app.get("/hello")
def say_hello():
    return {"message": "Hello, World!"}

@app.get("/blocking")
async def blocking():
    time.sleep(5)  # Simulate a blocking operation
    return {"message": "This is a blocking operation."}

@app.get("/non-blocking")
async def non_blocking():
    await asyncio.sleep(5)  # Simulate a non-blocking operation
    return {"message": "This is a non-blocking operation."}

@app.get("/sensor/{sensor_id}")
def sensor_reading(sensor_id: int, unit: str="C"):
    temp = 35
    if(unit not in ['C', 'F']):
        raise HTTPException(status_code=400, detail="The parameter must be either 'C' or 'F'.")
    if unit == 'F':
        temp = (temp * 9/5) + 32
    return {
        "sensor_id": sensor_id,
        "temperature": temp,
        "unit": unit
    }