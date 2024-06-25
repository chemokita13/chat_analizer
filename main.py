from fastapi import FastAPI
from chat import analyze_chat
from fastapi.middleware.cors import CORSMiddleware
import base64

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def hello():
    return {"Hello":"word"}

@app.post("/")
async def chat(data: dict):
    text = base64.b64decode(data["text"]).decode("utf-8")
    returner = analyze_chat(text)
    return returner