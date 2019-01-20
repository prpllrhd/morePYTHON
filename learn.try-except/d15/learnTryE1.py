#!/usr/bin/env python
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('calc.log')
logger.addHandler(file_handler)
formatter = logging.Formatter('%(asctime)s:%(message)s')
file_handler.setFormatter(formatter)

def div(a,b):
	return a/b

def main():
	x,y = 90,0
	try:
		divide = div(x,y)
	except ZeroDivisionError:
		logger.debug("you are attempting a zerodivision by dividing {} by {}".format(x,y))
	else:
		print divide

if __name__ == "__main__":
	main()
	
