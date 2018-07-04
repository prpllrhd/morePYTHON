#!/usr/bin/env python3
"""
example: using lambda key to sort a tuple of second field instead of first one
"""
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print (pairs)
