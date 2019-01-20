#!/usr/bin/env python
with open("textfile.txt") as fh:
	lines=fh.read()=
	dict = {}
	for each in lines:
		if dict.has_key(each):
			dict[each]+=1
		else:
			dict[each]=1
print dict.keys()
		
