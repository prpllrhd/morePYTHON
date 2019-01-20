#!/usr/bin/env python3
"""
python script to split a name based on "."
"""
def split_and_print_second(v1):
	second = v1.split(".")[1]+v1.split(".")[0]+v1.split(".")[2]
	return second

print split_and_print_second("gsbl300n01.blue.ygrid.yahoo.com")
