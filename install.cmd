@echo off
echo [KozoD] Welcome to KozoVideoDownloader installeur.
@ping localhost -n 2 >nul

echo [KozoD] [Console] Python 3 requires.


echo [KozoD] [Console] Pip upgrade.
@ping localhost -n 1 >nul
py -m pip install --upgrade pip


echo [KozoD] [Console] Installation of pytube lib.
@ping localhost -n 1 >nul
py -m pip install pytube


echo.
echo press a key to launch KozoD
pause > nul
start KozoD.py
