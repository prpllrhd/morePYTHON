#!/usr/bin/env python3
mylist=[("one",1),("two",2),("three",3),("four",4),("five",5),("six",6)]
d={}
for key,value in mylist:
	if value not in d:
		d[value] = []
	d[value].append(key)
print d.keys()
print d.values()
