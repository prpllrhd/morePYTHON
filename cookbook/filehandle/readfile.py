#!/usr/bin/env python
with open("/Users/samy/github/python/bigfile.txt") as fr:
	f=fr.read(100)
	while len(f)>0:
		print(f)
		f=fr.read(100)
