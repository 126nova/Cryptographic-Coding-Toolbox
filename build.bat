@echo off
pip install "cx_freeze==6.15.6"
pip install pyperclip

echo building...

python setup.py build
xcopy .\languages\ .\build\exe.win-amd64-3.11\languages\ /s /e /h /q
cd .\build\exe.win-amd64-3.11
del "frozen_application_license.txt"

pause