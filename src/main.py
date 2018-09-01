#!/usr/bin/env python

import sys
import os

import metadata

fail = False
target = sys.argv[1]

with os.scandir(target) as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            m = metadata.PyrationMetaData(entry.name)
            m.write_metadata(entry.path)
            new_path = os.path.join(target, "export", m.to_path())
            try:
                os.makedirs(os.path.dirname(new_path), exist_ok=True)
            except FileExistsError:
                pass
            try:
                os.rename(entry.path, new_path)
            except FileExistsError:
                fail = True
                print("{} already exists", new_path, file=sys.stderr)

if fail:
    sys.exit("Failed to rename at least one file.")
