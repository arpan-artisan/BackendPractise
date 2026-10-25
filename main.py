from fastapi import FastAPI, HTTPException
import time
import asyncio
import pydantic
import sqlite3

app = FastAPI()

# Initialize the database
connection = sqlite3.connect('practice.db')
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS readings (
    id INTEGER PRIMARY KEY,
    sensor_id INTEGER NOT NULL,
    temperature REAL NOT NULL,
    unit TEXT NOT NULL
)
""")
connection.commit()

class SensorModel(pydantic.BaseModel):
    sensor_id: int
    temperature: float
    unit: str = "C"

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
    temp = 40
    if(unit not in ['C', 'F']):
        raise HTTPException(status_code=400, detail="The parameter must be either 'C' or 'F'.")
    if unit == 'F':
        temp = (temp * 9/5) + 32
    return {
        "sensor_id": sensor_id,
        "temperature": temp,
        "unit": unit
    }

@app.post("/readings")
def create_reading(reading: SensorModel):
    if(reading.unit not in ['C', 'F']):
        raise HTTPException(status_code=400, detail="The parameter must be either 'C' or 'F'.")
    state = "normal"
    if reading.unit == 'F':
        reading.temperature = (reading.temperature - 32) * 5/9

    if(reading.temperature>40):
        state = "alert"

    return {
        "state": state
    }