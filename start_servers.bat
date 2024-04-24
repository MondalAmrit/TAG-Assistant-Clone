@echo off

echo Activating Virtual Environment...
rem Activate the virtual environment
call VirtualEnv\Scripts\activate

rem Install the latest packages
echo checking for latest packages...
pip install -r requirements.txt

echo Starting frontend...
rem Create frontend server in a separate command prompt window
start "Frontend Server" cmd /k "cd frontend && npm run dev"

echo Starting backend...
rem Create backend server in another separate command prompt window
start "Backend Server" cmd /k "cd backend && uvicorn main:app --reload"
