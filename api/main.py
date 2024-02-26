
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return "Hello, Ritika I am here"

@app.post("/")
async def post():
    return "Hello, Ritika I am here from post route"

@app.put("/")
async def put():
    return "Hello, Ritika I am here from put"