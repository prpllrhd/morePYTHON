#!/usr/bin/env python3
def getsquare(num):
	nums = (x*x for x in num)
	return nums

a = (getsquare(range(100000)))
for each in a:
	print (each)
