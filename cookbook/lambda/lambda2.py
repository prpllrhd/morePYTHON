#!/usr/bin/env python3
"""
using lambda map to get square all numbers in a list
map in lambda is used when you want to treat all numbers equally such as here where you want each number to be returned square of
"""
numbers = [1,2,3,4,5,6]
out = map(lambda x : x*2, numbers)
print (list(out))
