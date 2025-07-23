@echo off
:: Setzt das aktuelle Verzeichnis als Skriptverzeichnis
set SCRIPT_DIR=%~dp0
set PYTHON_SCRIPT="%SCRIPT_DIR%install_finance_libs.py"

:: Überprüft, ob das Skript als Administrator ausgeführt wird
NET SESSION >NUL 2>&1
IF %ERRORLEVEL% NEQ 0 (
    ECHO Dieses Skript muss als Administrator ausgeführt werden.
    ECHO Starte neu mit Administratorrechten...
    powershell -Command "Start-Process cmd -Verb RunAs -ArgumentList '/c \"%~f0\"'"
    EXIT /B
)

ECHO Starte Python-Installationsskript...
:: Führt das Python-Skript aus. Stellen Sie sicher, dass 'python' im PATH ist.
python %PYTHON_SCRIPT%

ECHO.
ECHO Skriptausführung beendet. Drücken Sie eine beliebige Taste, um fortzufahren...
PAUSE
