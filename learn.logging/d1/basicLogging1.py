#!/usr/bin/env python
def add(a,b):
	return a+b
def mul(a,b):
	return a*b
def div(a,b):
	return a/b
def substr(a,b):
	return a-b

def main():
	x,y = 18,3
	add_res = add(x,y)
	print "{} + {} = {}".format(x,y,add_res)

	mul_res = mul(x,y)
	print "{} X {} = {}".format(x,y,mul_res)

	div_res = div(x,y)
	print "{} / {} = {}".format(x,y,div_res)

	substr_res = substr(x,y)
	print "{} - {} = {}".format(x,y,substr_res)

if __name__ == "__main__":
	main()
