#!/bin/bash
# AI Learning Platform Frontend Deployment Package

cd "$(dirname "$0")"

echo "Starting frontend server..."
echo "Using nginx to serve static files on port 80"
echo ""

nginx -c "$(pwd)/nginx.conf" -g "daemon off;"
