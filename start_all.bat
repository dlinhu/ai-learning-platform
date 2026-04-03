@echo off
setlocal

echo Starting backend...
cd backend
if not exist venv (
  python -m venv venv
)
call venv\Scripts\activate.bat
pip install --no-cache-dir -r requirements.txt
cd ..

echo Starting frontend...
cd frontend
npm ci
set "VITE_API_URL=http://localhost:8000"
start "Frontend Dev" cmd /k "set VITE_API_URL=http://localhost:8000 && npm run dev"
echo Frontend started in a new window.

echo Backend is running in the current window if started above. End of setup.
"%COMSPEC%" /c exit
