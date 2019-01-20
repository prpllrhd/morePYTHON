#!/usr/bin/env python3.6
with open("bigfile.txt") as fh:
	fread = fh.read(100)
	while len(fread) > 0:
		print(fread , end="")
		fread = fh.read(100)

