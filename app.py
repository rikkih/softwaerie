from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def hello_world():
    return "Hello World"

