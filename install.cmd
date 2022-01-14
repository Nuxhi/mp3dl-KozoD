@echo off
Mode Con Cols=125 Lines=30
color 8
echo [KozoD] Welcome to KozoVideoDownloader installeur.
@ping localhost -n 2 >nul
echo.
echo.
echo [KozoD] [Console] Python 3 requires.
echo [KozoD] [Console] Pip upgrade.
@ping localhost -n 1 >nul
py -m pip install --upgrade pip

echo.
echo [KozoD] [Console] Installation of pytube lib.
@ping localhost -n 1 >nul
py -m pip install pytube
py -m pip install --upgrade pytube
echo.
echo.
echo [KozoD] [Tchek] All KozoD components were successfully installed.
echo Launch in 8s !
color 0f 
TIMEOUT /T 8 /NOBREAK
start KozoD.py
