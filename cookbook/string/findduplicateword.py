#!/usr/bin/env python3
import re
"""
example : read a file and if it encounters a word more than once next to each other, it print such numbers
"""
with open("file1.txt") as fh:
	searchq = re.compile(r"\b(\w+)\s*\1")
	fileread = fh.read()
	dups = searchq.findall(fileread)
print (dups)	
