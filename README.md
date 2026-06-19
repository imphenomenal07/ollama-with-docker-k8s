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
https://github.com/imphenomenal07/ollama-with-docker-k8s/blob/5d55500e6b246425bf27eb452dd99e59e1f976e3/Python%20Frontned%20API%20(FastAPI)/app.py

# Run Python Server

uvicorn app:app --host 0.0.0.0 --port 80

Example test:

http://PUBLIC_IP/ask?prompt=What%20is%20DevOps

Future Scaling
If traffic increases:
Load Balancer
+
Multiple EC2 instances
+
Docker containers
