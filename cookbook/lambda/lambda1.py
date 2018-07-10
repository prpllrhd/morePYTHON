#!/usr/bin/env python3
"""
example: using lambda key to sort a tuple of second field instead of first one
"""
import os
def script():
	pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
	pairs.sort(key=lambda pair: pair[1])
	print (pairs)
def help():
	print (__doc__)
def main():
	help()
#	script()

if __name__=="__main__":
	main()
	
