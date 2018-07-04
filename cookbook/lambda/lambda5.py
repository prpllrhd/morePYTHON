#!/usr/bin/env python3
"""
example: using lambda to reduce.
here sum of a list is returned basically to reduce the output to 1 from a list of numbers
"""
from functools import reduce
def help():
	print(__doc__)
def script():
	a=[1,2,3,4,5,6,7,7,8]
	sum = reduce(lambda x,y: x+y,a)
	#sum = reduce(lambda x,y: x+y,[1,2,3,4,5,6,7]) 
	print (sum)
def main():
#	script()
	help()
if __name__=="__main__":
	main()
