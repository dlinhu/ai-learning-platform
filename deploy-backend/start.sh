#!/bin/bash
# AI Learning Platform Backend Deployment Package

cd "$(dirname "$0")"

echo "Starting backend server..."

mkdir -p data

echo "Checking Python installation..."
python3 --version

echo ""
echo "Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "Starting server on port 8000..."
echo "API will be available at http://localhost:8000"
echo "API docs at http://localhost:8000/docs"
echo ""

python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8000
