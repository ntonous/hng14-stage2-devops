# FIXES.md

# Stage 2 DevOps Task – Complete Fixes & Implementation Report

## Overview

The starter repository contained multiple application bugs, poor production practices, missing infrastructure files, and non-container-friendly configurations.

This report documents all fixes completed during the task, including application debugging, Dockerization, environment management, and orchestration improvements.

---

# Project Services

The application consists of:

1. **Frontend** – Node.js / Express dashboard  
2. **API** – FastAPI backend service  
3. **Worker** – Python background job processor  
4. **Redis** – Queue + status storage

---

# SECTION A — Application Code Fixes

---

# 1. API Service Fixes (`api/main.py`)

## Fix 1 — Redis Host Hardcoded

### Original Problem

```python
redis.Redis(host="localhost", port=6379)
Issue

Inside containers, localhost refers to the API container itself, not Redis.

Resolution

Changed Redis host to:
host=os.getenv("REDIS_HOST", "redis")

Result
API can now connect to Redis container using Docker internal networking.

Fix 2 — Redis Port Hardcoded
Original Problem

Port was fixed to 6379.

Resolution

Changed to:
port=int(os.getenv("REDIS_PORT", 6379))

Result
Port is now configurable.

Fix 3 — Missing Health Endpoint
Resolution
write a health endpoint code to include health check

@app.get("/health")
def health():
    return {"status": "ok"}

  Result

Used by Docker healthcheck system.

Fix 4 — Incorrect HTTP Response for Missing Jobs
Original Problem

Returned HTTP 200 OK even when job did not exist.

Resolution

Updated to proper 404 Not Found.

Result
Correct API behavior and cleaner client handling.

2. Worker Service Fixes (worker/worker.py)
Fix 1 — Redis Host Hardcoded

Changed from:
localhost

To:
os.getenv("REDIS_HOST", "redis")

Fix 2 — Removed Unused Import

Removed:
import signal

This reduced lint warnings and unnecessary code.

Fix 3 — Redis Reconnection Handling

Added retry logic when Redis is unavailable.

Result

Worker does not fail permanently if Redis starts late.

Fix 4 — Error Handling During Job Processing

Wrapped processing logic in exception handling.

Result

One failed job no longer crashes the worker container.

Fix 5 — Added Processing Status

Before marking completed, worker now sets:

processing

Tnen later:

completed

Result

Improved job lifecycle visibility.

3. Frontend Fixes (frontend/app.js)
Fix 1 — API URL Hardcoded
Original Problem

const API_URL = "http://localhost:8000";

Resolution

Changed to:

const API_URL = process.env.API_URL || "http://api:8000";

Result

Frontend container now reaches API service correctly.

Fix 2 — Frontend Port Hardcoded

Changed:

3000

To:

process.env.PORT || 3000

Result

Port configurable through environment variables.

Fix 3 — Added /health Endpoint

Added route for Docker healthchecks.

Fix 4 — Bound Server to 0.0.0.0
Why

Allows external access from Docker host.

Fix 5 — Improved Error Messages

Added clearer frontend error handling and logging.

4. Frontend Package Improvements (frontend/package.json)
Added:
Lint Script
"lint": "eslint ."

Test Script Placeholder

"test": "echo tests pending"

ESLint Dev Dependency

Added ESLint for CI lint stage.

Node Engine Requirement

Defined supported Node version.

SECTION B — Repository Hygiene & Security
5. Removed Committed .env

A .env file existed inside starter repository.

Risk

Secrets should never be committed.

Resolution

Removed .env and replaced with:
.env.example

6. Added .gitignore

Created:
.env
*.env
__pycache__/
*.pyc
node_modules/
coverage/
dist/
.vscode/
.DS_Store
*.log

Purpose

Prevent accidental commits of:

secrets
cache files
logs
dependencies
build artifacts
SECTION C — Environment Configuration
7. Added .env.example

Created root template:
REDIS_HOST=redis
REDIS_PORT=6379
API_PORT=8000
FRONTEND_PORT=3000
API_URL=http://api:8000
PORT=3000

Purpose

Documents required variables for setup.

SECTION D — Dockerization
8. Added API Dockerfile (api/Dockerfile)

Implemented:

Python slim base image
Dependency installation
Non-root runtime user
Port 8000 exposed
Healthcheck added
Starts with Uvicorn
9. Added Worker Dockerfile (worker/Dockerfile)

Implemented:

Python slim image
Non-root user
Runs worker process
Healthcheck support
10. Added Frontend Dockerfile (frontend/Dockerfile)

Implemented:

Node Alpine image
Production dependency install
Non-root user
Port 3000 exposed
Healthcheck route tested
SECTION E — Docker Compose Orchestration
11. Added docker-compose.yml

Configured services:

redis
api
worker
frontend
Features Implemented
Internal Network

Named bridge network for secure service communication.

Dependency Ordering

Containers wait for healthy dependencies.

Redis Security

Redis not exposed publicly.

Resource Limits

CPU and memory limits added for all services.

Restart Policies
restart: unless-stopped

Environment Variables

All config loaded from .env

SECTION F — Functional Verification
12. Successful End-to-End Testing
Verified:
Frontend Loaded
http://localhost:3000

Job Submission Worked

Dashboard successfully created jobs.

Queue Processing Worked

Worker received jobs through Redis.

Status Updates Worked

Jobs moved from:
queued → processing → completed

Healthchecks Passed

Containers reported healthy state.

Final Outcome

The broken starter repository was fully transformed into a working production-style containerized microservices application.

Deliverables Completed
Fixed application bugs
Added environment-based config
Added healthchecks
Added Dockerfiles
Added Docker Compose stack
Improved repository hygiene
Added documentation
Verified full application workflow
Status

✅ Stage 2 Task Successfully Completed