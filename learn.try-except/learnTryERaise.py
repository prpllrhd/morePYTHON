#!/usr/bin/env python
##raising a specific error. just for example.
try:
	a = open("file.txt")
except:
	raise ZeroDivisionError
