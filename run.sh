#!/bin/sh
dir=~/.local/share/pyration/
find $dir -maxdepth 1 -type f -print0 | xargs -0 -I track python src/main.py track
