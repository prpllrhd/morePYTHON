#!/usr/bin/env python
##in a file find all instances of duplicate words
import re
with open("experimentfile.py","r") as file:
	fh = file.read()
	pattern = re.compile(r"(\w+)\s\1")
	findduplicates = pattern.findall(fh)
	for word in findduplicates:
		print word
