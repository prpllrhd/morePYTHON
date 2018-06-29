#!/usr/bin/env python
#####simple program to print 10 fibonacci numbers
a,b=0,1
fib=a+b
n=7
print "{}".format(a)
print "{}".format(b)
print "{}".format(fib)
for i in range(1,n):
	a=b
	b=fib
	fib=a+b
	print "{}".format(fib)

