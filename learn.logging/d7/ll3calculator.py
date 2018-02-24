#!/usr/bin/env python
import logging
import ll3employee
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARN)

file_handler=logging.FileHandler("ll3-calculator.log")
file_formatter = logging.Formatter('%(created)f:%(levelname)s:%(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

def add(a,b):
	return a+b

def subst(a,b):
	return a-b

def mul(a,b):
	return a-b

def div(a,b):
	return a/b


def main():
	x,y=10,0
	
	sum = add(x,y)
	logger.warn("{} + {} = {}".format(x,y,sum))

	minus = subst(x,y)
	logger.warn("{} - {} = {}".format(x,y,minus))

	multiply = mul(x,y)
	logger.warn("{} X {} = {}".format(x,y,multiply))

	try:
		division=div(x,y)
	except ZeroDivisionError:
		logger.exception("trying to divide {} by {}".format(x,y))
	else:
		logger.warn("{} / {} = {}".format(x,y,division))

		
if __name__ == "__main__":
	main()
