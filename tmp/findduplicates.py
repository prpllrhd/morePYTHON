#!/usr/bin/env python3
import re
with open("files.txt") as fh:
	fileread = fh.read()
	searchq = re.compile(r"(\w+)\s\1")
	search = searchq.findall(fileread)
	for each in search:
		print (each)
	
