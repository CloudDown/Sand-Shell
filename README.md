# Sand-Shell

Windows Python shell prototype. The app lives in `Sand-Shell/` and the installer copies that folder to `C:\Windows\Sand-Shell`.

## Layout

- `Sand-Shell.py` — launcher / mode picker
- `shell.py` — command loop
- `settings.py` — settings mode
- `game.py` — extra mode
- `help.html` — command list
- `config.cfg` — color config (`[COLOR]` `Title`, `Command`)
- `install.bat` / `uninstall.bat` — Windows install helpers

Hardcoded paths assume `C:\Windows\Sand-Shell`.

## Check syntax

```
python -m py_compile Sand-Shell/*.py
```
