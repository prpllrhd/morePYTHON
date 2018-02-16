#!/usr/bin/env python
import logging
import employee
logging.basicConfig(filename="basicLogging2.log",level=logging.DEBUG,
	format='%(asctime)s:%(name)s:%(message)s')
def add(a,b):
	return a+b
def mul(a,b):
	return a*b
def div(a,b):
	return a/b
def subtr(a,b):
	return a-b

def main():
	x,y = 18,3
	add_result = add(x,y)
	logging.critical("{} + {} = {}".format(x,y,add_result))
	
	mul_result = mul(x,y)
	logging.debug("{} X {} = {}".format(x,y,mul_result))

	div_result = div(x,y)
	logging.debug("{} / {} = {}".format(x,y,div_result))

	subtr_result = subtr(x,y)
	logging.debug("{} - {} = {}".format(x,y,subtr_result))

if __name__ == "__main__":
	main()

