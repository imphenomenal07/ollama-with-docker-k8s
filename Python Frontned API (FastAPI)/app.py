from fastapi import FastAPI
import requests

app = FastAPI()

OLLAMA_URL = "http://localhost:11434/api/generate"


@app.get("/")
def home():
    return {"message": "Ollama 3B API is running"}


@app.get("/ask")
def ask(prompt: str):
    payload = {
        "model": "llama3:3b",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    return response.json()
