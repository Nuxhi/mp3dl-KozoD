@echo off
echo [KozoD] Welcome to KozoDownload installeur.
@ping localhost -n 2 >nul

echo [KozoD] [Console] Python 3 requires.
findstr 
echo [KozoD] [Console] Installation of pytube lib.
@ping localhost -n 1 >nul
py -m pip install pytube

echo.
echo appuyer sur une touche pour lancer KozoD
pause > nul
start KozoD.py