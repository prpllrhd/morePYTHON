#!/usr/bin/env python
####1. take input from user for a number and print if it is a prime number
####2. print numbers from 1-100 and print the prime numbers
####3. take input from user for a range and print prime numbers
####4. define a function and do step 1,2,3
num1 = input("Input a number: ")
num2 = input("Input another number: ")


for x in range(num1,num2):
    prime = True
    for i in range(2,x):
        if (x%i==0):
            prime = False
    if prime == True:
       print x

print "Done......"
