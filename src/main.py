#!/usr/bin/env python
import metadata
import sys
import os
m = metadata.PyrationMetaData(sys.argv[1])
try:
    os.mkdir(m.artist)
except FileExistsError:
    pass
try:
    os.rename(m.orig, m.to_path())
except FileExistsError:
    print("{} already exists", m.to_path(), file=sys.stderr)
