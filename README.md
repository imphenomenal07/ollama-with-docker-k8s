# Deploying Ollama 3B Model on AWS EC2 using Docker

Deploying OLLAMA 3.2 - 3B model on AWS along with creating Docker Container with official Docker Ollama image

# Architecture

Users ➡️ Public IP / DNS ➡️ Python API (FastAPI) ➡️ Ollama Docker Container ➡️ EC2 Instance

# Recommended AWS Configuration

AMI: Amazon Linux 2023

Instance Type: **c6a.xlarge**
Specs:
- 4 vCPU
- 8 GB RAM

Estimated Cost: ~$110/month

Storage:
EBS gp3
Size: 75 GB

# Security Group

Allow inbound ports:

SSH ➡️ 22

Eeb frontend ➡️ 80

Ollama API ➡️ 11434

Source: 0.0.0.0/0 (testing only)

# Connect to EC2
ssh -i key.pem ec2-user@PUBLIC_IP

# Install Docker

sudo yum update -y

sudo yum install docker -y

sudo systemctl start docker

sudo systemctl enable docker

sudo usermod -aG docker ubuntu

# Run Ollama Docker Container

mkdir ollama-data

docker run -d -p 11434:11434 -e OLLAMA_HOST=0.0.0.0 -v ~/ollama-data:/root/.ollama --name ollama ollama/ollama

# Download 3B Model

docker exec -it ollama ollama pull llama3:3b

# Test Ollama API

curl http://localhost:11434/api/generate -d '{

"model": "llama3:3b",

"prompt": "Explain DevOps"

}'

# Python Frontend API (FastAPI)

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
