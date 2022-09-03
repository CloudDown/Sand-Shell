@echo off
color 6
echo Downloading Sand-Shell...
powershell.exe Move-Item -Path "soth" -Destination "C:\Windows"
powershell.exe Move-Item -Path "Sand-Shell.py" -Destination "C:\Windows"
timeout 3
set TARGET='C:\Windows\Sand-Shell.py'
set SHORTCUT='%USERPROFILE%\Desktop\Sand-Shell.lnk'
set PWS=powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile

%PWS% -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut(%SHORTCUT%); $S.TargetPath = %TARGET%; $S.Save()"