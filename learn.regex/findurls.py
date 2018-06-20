#!/usr/bin/env python
import re
pattern = re.compile(r".*?\.\w{3}")
with open("experimentfile.py","r") as file:
	fh = file.read()
	search = pattern.findall(fh)
	print search
	

