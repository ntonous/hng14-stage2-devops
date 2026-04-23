# hng14-stage2-devops
# 🚀 Stage 2 DevOps Task — Containerized Microservices Job Processor

## 📌 Overview

This project is a **containerized microservices application** designed to simulate a job processing system. It consists of multiple services working together to accept, queue, process, and track jobs in real-time.

The objective of this task was to transform a **broken starter repository** into a **production-ready system** by:

- Fixing application bugs
- Containerizing services using Docker
- Orchestrating services with Docker Compose
- Implementing health checks and environment-based configuration
- Ensuring secure and scalable architecture

---

## 🧱 Architecture

The application is composed of four core services:

### 1. Frontend (Node.js / Express)
- Provides a simple web interface for submitting jobs and tracking status
- Communicates with the API service

### 2. API (FastAPI)
- Handles job creation and status retrieval
- Pushes jobs into Redis queue

### 3. Worker (Python)
- Consumes jobs from Redis queue
- Processes jobs asynchronously
- Updates job status

### 4. Redis
- Acts as a message queue and temporary data store

---

## 🔄 System Flow

1. User submits a job via frontend
2. Frontend sends request to API
3. API pushes job into Redis queue
4. Worker pulls job from Redis and processes it
5. Worker updates job status
6. Frontend polls API for job status

---

## ⚙️ Technologies Used

- **Docker & Docker Compose**
- **FastAPI (Python)**
- **Node.js / Express**
- **Redis**
- **Uvicorn**
- **ESLint & Flake8 (for CI readiness)**

---

## 📁 Project Structure

hng14-stage2-devops/
│
├── api/
│ ├── main.py
│ ├── requirements.txt
│ └── Dockerfile
│
├── frontend/
│ ├── app.js
│ ├── package.json
│ ├── views/
│ └── Dockerfile
│
├── worker/
│ ├── worker.py
│ ├── requirements.txt
│ └── Dockerfile
│
├── docker-compose.yml
├── .env.example
├── .gitignore
├── FIXES.md
└── README.md


---

## 🔐 Environment Variables

Create a `.env` file in the root directory using the template below:

REDIS_HOST=redis
REDIS_PORT=6379
API_PORT=8000
FRONTEND_PORT=3000
API_URL=http://api:8000

PORT=3000


⚠️ `.env` is not committed for security reasons. Use `.env.example` as reference.

---

## 🐳 Running the Application

### Prerequisites

- Install Docker Desktop  
- Ensure Docker Engine is running  

### Steps

1. Clone the repository:

```bash
git clone https://github.com/chukwukelu2023/hng14-stage2-devops
cd hng14-stage2-devops

Create .env file (see above)
Start the application:

docker compose up --build

🌐 Access the Application

Once running:

Frontend: http://localhost:3000
API: http://localhost:8000
🧪 Testing the Application
Open the frontend in your browser
Click Submit New Job
Observe:
Job ID generated
Status updates from queued → processing → completed
❤️ Health Checks

Each service includes a health check endpoint or mechanism:

API: /health
Frontend: /health
Redis: redis-cli ping
Worker: process-based check

These ensure proper service readiness and stability.

🔒 Security Considerations
No secrets or .env files are committed
All services run as non-root users
Redis is not exposed publicly
Environment variables used for configuration
🛠 Improvements Made
Removed hardcoded configurations
Introduced environment variables
Fixed inter-service communication issues
Added Dockerfiles for all services
Implemented health checks
Improved error handling and logging
Structured project for scalability

Full details are available in:

👉 FIXES.md

📦 Deployment Notes

This application is production-ready and can be deployed on:

VPS (Ubuntu)
Cloud VM (AWS, Azure, GCP)

Ensure Docker is installed and run:

docker compose up -d

📌 Key DevOps Concepts Demonstrated
Containerization
Service orchestration
Internal networking
Health checks
Environment configuration
Microservices architecture
Debugging and system hardening
✅ Status

✔ Fully functional
✔ Dockerized
✔ Tested end-to-end
✔ Ready for submission

👤 Author

Hezekiah Umoh

Final Note

This project demonstrates practical DevOps skills in transforming a flawed system into a robust, production-ready microservices architecture.