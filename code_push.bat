@echo off

rem Ask for commit message
set /p commit_msg="Commit message: "

rem Set default commit message if user input is empty
if "%commit_msg%" == "" (
    set commit_msg="Automated commit"
)

rem Execute Git commands in Git Bash
git add .
git commit -m "%commit_msg%"
git push