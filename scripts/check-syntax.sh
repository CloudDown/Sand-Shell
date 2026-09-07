#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 -m py_compile \
  Sand-Shell/Sand-Shell.py \
  Sand-Shell/shell.py \
  Sand-Shell/settings.py \
  Sand-Shell/game.py \
  Sand-Shell/install-app.py
echo ok
