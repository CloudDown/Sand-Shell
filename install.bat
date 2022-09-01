@echo off
powershell.exe Move-Item -Path "Sand-Shell.py" -Destination "C:\Windows"
powershell.exe Move-Item -Path "config.ini" -Destination "C:\Windows"
powershell.exe Move-Item -Path "help.html" -Destination "C:\Windows"
powershell.exe Move-Item -Path "style.css" -Destination "C:\Windows"
powershell.exe Move-Item -Path "log.txt" -Destination "C:\Windows"
timeout 3
set TARGET='C:\Windows\Sand-Shell.py'
set SHORTCUT='%USERPROFILE%\Desktop\Sand-Shell.lnk'
set PWS=powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile

%PWS% -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut(%SHORTCUT%); $S.TargetPath = %TARGET%; $S.Save()"