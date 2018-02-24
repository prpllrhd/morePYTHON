#!/usr/bin/env python
##### all output sent to console
##### use of python:logging:exception
import logging
def addnum(a,b):
	return a+b
def mulnum(a,b):
	return a*b
def divnum(a,b):
	return a/b
def subnum(a,b):
	return a-b

def main():
	x,y=90,0
	sum=addnum(x,y)
	logging.warn("Sum of {} and {} is {}".format(x,y,sum))

	minus=subnum(x,y)
	logging.warn("substrack of {} and {} is {}".format(x,y,minus))

	try:
		div=divnum(x,y)
	except ZeroDivisionError:
		logging.exception("Tried to divide by zero")
	else:
		logging.warn("division of {} and {} is {}".format(x,y,div))

	mul=mulnum(x,y)
	logging.warn("multiply of {} and {} is {}".format(x,y,mul))

if __name__ == "__main__":
	main()
