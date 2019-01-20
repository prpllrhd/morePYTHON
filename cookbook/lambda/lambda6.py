#!/usr/bin/env python3
"""
use reduce on an existing input of data
"""
from functools import reduce
def script():
	f = lambda a,b: a if(a>b) else b
	out = reduce(f,range(10000))
	print (out)
def help():
	print(__doc__)
def main():
	help()
	script()
if __name__=="__main__":
	main()
