# HNG Stage 2 DevOps Task — Containerized Job Processor

![CI Pipeline](https://github.com/ntonous/hng14-stage2-devops/actions/workflows/main.yml/badge.svg)

##  Project Overview

This project is a **production-ready containerized microservices job processing system** built for the **HNG Stage 2 DevOps Task**.

The application was audited, repaired, optimized, containerized, and automated with a complete CI/CD pipeline using GitHub Actions.

Users can submit jobs from a web dashboard, jobs are processed asynchronously by a worker service, and statuses are tracked in real time.

---

## Tech Stack

| Component      | Technology        |
| -------------- | ----------------- |
| Frontend       | Node.js + Express |
| Backend API    | FastAPI           |
| Worker Service | Python            |
| Queue / Cache  | Redis             |
| Containers     | Docker            |
| Orchestration  | Docker Compose    |
| CI/CD          | GitHub Actions    |

---

## Architecture

```text
User Browser
     ↓
Frontend Dashboard (Port 3000)
     ↓
FastAPI API Service (Port 8000)
     ↓
Redis Queue
     ↓
Python Worker
```

---

## Key Features

* Submit background jobs from dashboard
* Real-time job tracking
* Redis queue processing
* Multi-container microservices architecture
* Docker health checks
* Automatic restart policies
* Environment variable configuration
* Security image scanning
* Full CI/CD automation
* Production-ready deployment workflow

---

## Project Structure

```text
hng14-stage2-devops/
│── api/
│── frontend/
│── worker/
│── tests/
│── .github/workflows/main.yml
│── docker-compose.yml
│── .env.example
│── FIXES.md
│── README.md
```

---

## 🔄 CI/CD Pipeline

The project uses a complete multi-stage GitHub Actions pipeline:

```text
lint → test → build → security-scan → integration-test → deploy
```

### Pipeline Stages

### ✅ Lint

* Python linting with flake8
* JavaScript linting with ESLint
* Dockerfile linting with Hadolint

### ✅ Test

* Unit tests with pytest
* Coverage reports generated automatically

### ✅ Build

* API Docker image
* Worker Docker image
* Frontend Docker image

### ✅ Security Scan

* Trivy image vulnerability scanning

### ✅ Integration Test

* Full application stack launched with Docker Compose
* API + frontend health checks
* Job submission test

### ✅ Deploy

* Simulated rolling deployment on `main`

---

## ⚙️ Environment Variables

Create `.env`

```env
REDIS_HOST=redis
REDIS_PORT=6379

API_PORT=8000
FRONTEND_PORT=3000

API_URL=http://api:8000
```

---

## Run Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/ntonous/hng14-stage2-devops.git
cd hng14-stage2-devops
```

### 2️⃣ Start Application

```bash
docker compose up --build -d
```

### 3️⃣ Verify Containers

```bash
docker compose ps
```

Expected:

* frontend → healthy
* api → healthy
* worker → healthy
* redis → healthy

---

## Application Access

### Frontend Dashboard

```text
http://localhost:3000
```

### API Health Check

```text
http://localhost:8000/health
```

---

## Job Flow Test

1. Open dashboard
2. Submit new job
3. Worker processes queue
4. Status updates to:

```text
completed
```

---

## Security Improvements

* Containers run as non-root users
* Vulnerability scans with Trivy
* Lightweight base images
* Health monitoring enabled
* Environment secrets externalized

---

## DevOps Skills Demonstrated

* CI/CD pipeline engineering
* Docker optimization
* Microservices orchestration
* Security scanning
* Automated testing
* Integration testing
* GitHub Actions workflows
* Production troubleshooting
* Deployment automation

---

## Deliverables

* Source code
* Dockerfiles
* Docker Compose
* GitHub Actions pipeline
* README.md
* FIXES.md

---

## 👤 Author

**Hezekiah Umoh**

GitHub: https://github.com/ntonous

---

## 🎯 Final Note

This project demonstrates practical DevOps ability in transforming a broken system into a secure, scalable, containerized production-ready platform with full CI/CD automation.
