cd src

@echo off
ipconfig | findstr /R /C:"IPv4 Address"

python main.py

pause