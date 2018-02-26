#!/usr/bin/env python
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('calc.log')
logger.addHandler(file_handler)
formatter = logging.Formatter('%(asctime)s:%(message)s')
file_handler.setFormatter(formatter)
def add(a,b):
	return a+b

def div(a,b):
	return a/b

def main():
	x,y = 90,0
	sum = add(x,y)
	logger.debug("sum of {} and {} is {}".format(x,y,sum))
	
	try:
		divide = x/y
	except ZeroDivisionError:
		logger.warn("you are attempting a zerodivision by dividing {} by {}".format(x,y))
	else:
		print divide

if __name__ == "__main__":
	main()
	
