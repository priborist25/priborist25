import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/hui")
async def index():
    return "hui"

@app.get("/")
async def index():
    return "Hello from FastAPI"

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True, port=5000)