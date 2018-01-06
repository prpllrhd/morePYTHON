#!/usr/bin/env python
import logging 
def add_no(a,b):
	return a + b

def mul_no(a,b):
	return a * b

def div_no(a,b):
	return a / b

def substract(a,b):
	return a - b

def main():
	num1 = 25
	num2 = 10

	add_result = add_no(num1,num2)
	logging.warning("Add : {} + {} = {}".format(num1,num2,add_result))

	mul_result = mul_no(num1, num2)
	print("Mul: {} x {} = {}".format(num1, num2, mul_result))

	div_result = div_no(num1, num2)
	print ("Div: {} / {} = {}".format(num1 ,num2 , div_result))

	subst_result = substract(num1, num2)
	print ("Substract : {} - {} = {}".format(num1,num2,subst_result))

if __name__ == "__main__":
	main()
