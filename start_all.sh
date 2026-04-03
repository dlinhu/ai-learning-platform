#!/usr/bin/env bash
set -euo pipefail

echo "Starting backend..."
cd backend

# Setup virtual environment if not present
if [ ! -d "venv" ]; then
  python -m venv venv
fi
source venv/bin/activate

# Install requirements
pip install --no-cache-dir -r requirements.txt

# Run backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!
echo "Backend started (PID: $BACKEND_PID)"

cd ..

echo "Starting frontend..."
cd frontend

# Install dependencies
npm ci

# Ensure API URL points to backend
export VITE_API_URL=http://localhost:8000

# Run frontend dev server
npm run dev &
FRONTEND_PID=$!
echo "Frontend started (PID: $FRONTEND_PID)"

echo "All services started. Backend PID=$BACKEND_PID, Frontend PID=$FRONTEND_PID"
