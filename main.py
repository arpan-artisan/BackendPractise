from fastapi import FastAPI
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