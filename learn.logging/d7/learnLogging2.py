#!/usr/bin/env python
#####python:basicConfig to sent output to file, set up formatting and levels
import logging
logging.basicConfig(filename="calculator.log",level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')
def addnum(a,b):
	return a+b

def subnum(a,b):
	return a-b

def mulnum(a,b):
	return a*b

def divnum(a,b):
	return a/b

def main():
	x,y=90,15
	add = addnum(x,y)
	logging.debug("{} + {} = {}".format(x,y,add))

	mul = mulnum(x,y)
	logging.debug("{} * {} = {}".format(x,y,mul))

	div = divnum(x,y)
	logging.debug("{} / {} = {}".format(x,y,div))

	sub = subnum(x,y)
	logging.debug("{} - {} = {}".format(x,y,sub))

if __name__ == "__main__":
	main()
	
	
	
	
	
