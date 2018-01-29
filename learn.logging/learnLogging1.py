#!/usr/bin/env python
import logging
#logger = logging.getLogger("__main__")
#logger.setLevel(logging.INFO)
#file_handler=logging.FileHandler("file1.log")
#logger.addHandler(file_handler)
logging.basicConfig(filename='file.log',level=logging.INFO)
def add(a,b):
	return a+b

def multiply(a,b):
	return a*b

def division(a,b):
	return a/b

num_a,num_b=20,10
add_result = add(num_a,num_b)
logging.info("add: {} + {} = {}".format(num_a,num_b,add_result))

mul_result=multiply(num_a,num_b)
logging.info("multiply: {} * {} = {}".format(num_a,num_b,mul_result))

div_result=division(num_a,num_b)
logging.info("div: {} / {} = {}".format(num_a,num_b,div_result))
