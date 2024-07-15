@echo off
@title Py My Http Server Lib Installer
rem Bu .bat dosyası ile Python paketleri kuruluyor.
rem Python betiği için bir sanal ortam oluştur
python -m venv venv
rem Sanal ortamı etkinleştir
call venv\Scripts\activate
rem Paketleri kur
pip install httpserver
pip install colorama
pip install sockets
pip install time
pip install json
pip install sys
pip install os
rem İstediğiniz kadar paket ekleyebilirsiniz.
rem Sanal ortamı devre dışı bırak
deactivate
rem .bat dosyası tamamlandı.
pause