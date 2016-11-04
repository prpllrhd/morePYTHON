#!/usr/bin/env python
import re
dict={}
for line in open("/etc/passwd"):
  if not re.search("^#",line):continue
  line = line.strip()
  flds=()
  flds = re.split(':',line)
  dict.setdefault(flds[0],[]).append(flds[1:3])
print dict
