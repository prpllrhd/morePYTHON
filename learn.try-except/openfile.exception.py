#!/usr/bin/env python
try:
	with open("/tmp/a.txt","r") as x:
		a = x.read()
	print a
except Exception as e:
	print "Errorrrrrr {} ".format(e)
