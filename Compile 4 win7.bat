echo off
C:\Users\akash\AppData\Local\Programs\Python\Python38\Scripts\pyinstaller  --clean --hidden-import=pyttsx3.drivers --hidden-import=pyttsx3.drivers.sapi5 --onefile --noconsole win.py

del /s /q /f RAT.spec
rmdir /s /q __pycache__
rmdir /s /q build

:cmd
pause null