#!/usr/bin/env python3
"""
example: use of lambda key to sort a list of names based on last character of each name in the list
"""
names = ["sameer","rakhee","sharad","alka"]
names.sort(key = lambda name: name[::-1])
print (names)
