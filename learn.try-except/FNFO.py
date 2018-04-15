#!/usr/bin/env python
try:
	with open("ttt.txt") as fh
except FileNotFoundError, e:
	print "You entered a non existant file"
