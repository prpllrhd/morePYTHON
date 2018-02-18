#!/usr/bin/env python
try:
	raise Exception("issue opening file")
	f = open("a.txt")
except Exception as EE:
	print EE
try:
	b = bad_var
	print b
except NameError as e:
	print e
try:
	count = 0
	while count<10:
		count += 1
		print "Hello"
		#if count == 20:
		#	break
except:
	print "You got it wrong"
