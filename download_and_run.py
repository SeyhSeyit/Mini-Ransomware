import os
import requests
import subprocess

# GitHub'daki dosyanızın URL'si
url = "https://raw.githubusercontent.com/kullanici_adi/depo_adi/main/main.py"

# Dosyayı indirme
response = requests.get(url)
with open("main.py", "wb") as file:
    file.write(response.content)

# Dosyayı çalıştırma
subprocess.run(["python", "main.py"])
