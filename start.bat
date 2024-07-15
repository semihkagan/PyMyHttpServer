@echo off
@title HTTP Web Server Console
echo Starting...
echo HTTP Server Console Started!
set python_script_path=".src/main.py"
python %python_script_path% --nogui
exit