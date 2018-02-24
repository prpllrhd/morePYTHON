#!/usr/bin/env python
import logging
import employee
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s:%(name)s:%(message)s")
file_handler = logging.FileHandler("basicLogging4.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
#logging.basicConfig(filename="basicLogging2.log",level=logging.DEBUG,
#	format='%(asctime)s:%(name)s:%(message)s')
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
	logger.critical("{} + {} = {}".format(x,y,add_result))
	
	mul_result = mul(x,y)
	logger.debug("{} X {} = {}".format(x,y,mul_result))

	div_result = div(x,y)
	logger.debug("{} / {} = {}".format(x,y,div_result))

	subtr_result = subtr(x,y)
	logger.debug("{} - {} = {}".format(x,y,subtr_result))

if __name__ == "__main__":
	main()
