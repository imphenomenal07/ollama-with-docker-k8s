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

22 -> SSH
80 -> Web frontend
11434 -> Ollama API

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
