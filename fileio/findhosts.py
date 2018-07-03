#!/usr/bin/env python
###tag:fnmatch;tag:string
from fnmatch import fnmatch,fnmatchcase
hosts = [
"gsbl300n00.blue.ygrid.yahoo.com","gsbl300n01.blue.ygrid.yahoo.com",
"gsbl300n02.blue.ygrid.yahoo.com","gsbl300n03.blue.ygrid.yahoo.com",
"gsbl300n04.blue.ygrid.yahoo.com","gsbl300n05.blue.ygrid.yahoo.com",
"gsbl300n00.blue.ygrid.yahoo.com","gsbl300n00.blue.ygrid.yahoo.com",
"gsbl300n07.blue.ygrid.yahoo.com","gsbl300n08.blue.ygrid.yahoo.com",
]

matches = []
unmatches = []
for each in hosts:
	#if (fnmatchcase(each,"gsbl300n[0-4][3-9]*")):
	if (fnmatchcase(each,"gsbl301n0[0-5].blue.ygrid.yahoo.com")):
		matches.append(each)
	else:
		unmatches.append(each)
if len(unmatches) < 1:
	print ("all matched")
	print (matches," hosts exists")
elif len(matches) < 1:
	print ("none matched")
	print (unmatches," hosts added")
else:
	print (matches," hosts exists")
	print (unmatches," hosts added")
