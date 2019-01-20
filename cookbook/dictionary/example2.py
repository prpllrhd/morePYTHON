#!/usr/bin/env python3
"""
simple appending to dictionary using defaultdict module
"""
import sys
if sys.argv[1] == "--help":
	print (__doc__)
	exit(1)
mylist=[("one",1),("two",2),("three",3),("four",4),("five",5),("six",6)]
from collections import defaultdict
d = defaultdict(list)
for key,value in mylist:
	d[key].append(value)

print d.keys()
print d.values()
