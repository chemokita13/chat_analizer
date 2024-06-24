from fastapi import FastAPI
from chat import analyze_chat
import base64

app = FastAPI()

@app.get("/")
def hello():
    return {"Hello":"word"}

@app.post("/")
async def chat(data: dict):
    text = base64.b64decode(data["text"]).decode("utf-8")
    print(text)
    returner = analyze_chat(text)
    return returner