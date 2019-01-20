#!/usr/bin/env python
import re
search=re.compile(r"\d{3}[-.]\d{3}[-.]\d{4}")
with open ("experimentfile.py") as fh:
	fileread = fh.read()	
	matches = search.finditer(fileread)
	for each in matches:
		print each
	
