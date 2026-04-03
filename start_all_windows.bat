@echo off
setlocal

echo Starting backend in a new window...
start "Backend Dev" cmd /k "cd /d backend & if exist venv\\Scripts\\activate.bat (call venv\\Scripts\\activate.bat) else (echo venv not found) & uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"

echo Starting frontend in a new window...
start "Frontend Dev" cmd /k "cd /d frontend & npm ci & set VITE_API_URL=http://localhost:8000 & npm run dev -- --port 3000"

echo Both services should be starting in separate windows.
endlocal
