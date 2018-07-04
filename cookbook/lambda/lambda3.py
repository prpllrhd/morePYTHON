#!/usr/bin/env python3
"""
example: using lambda filter to put a condition on a list. return only those numbers that are % 2 
filter in lambda is used when u want to filter numbers using a condition like here
"""
list_a = [1, 2, 3, 4, 5]

filter_obj = filter(lambda x: x % 2 == 0, list_a) # filter object <filter at 0x4e45890>

even_num = list(filter_obj) # Converts the filer obj to a list

print(even_num) # Output: [2, 4]
