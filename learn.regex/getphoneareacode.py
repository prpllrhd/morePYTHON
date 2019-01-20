#!/usr/bin/env python
import logging
import re
with open("phonenum.txt","r") as file:
	fh = file.read()
	pattern = re.compile(r"(\d{3}).\d{3}.\d{4}")
	search = pattern.findall(fh)
for each in search:
	repl = re.sub(each,each+"-xxx-xxxx",each)
	print repl
	
	
	
