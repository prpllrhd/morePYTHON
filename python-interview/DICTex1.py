#!/usr/bin/env python
####regex and dictionary
#### read a file and find ip address and count instances of ip addresses.
#### now write to get top n ip addresses based on argparse input
import re
import pprint
pp = pprint.PrettyPrinter(indent=4)
se = []
d = dict()
with open("file1.txt","r") as fh:
	for i in fh.readlines():
		search = (re.search(r"(\[\d+\])",i))
	#	se.append(search.group(1))
		if d.has_key(search.group(1)):
			d[search.group(1)] +=1
		else:
			d[search.group(1)]=1
pprint.pprint(d,depth=3,width=60)
print(d)

		
		
#print se
#print  str(se).strip('[]')
#print ','.join(se)
#print '\n'.join(se)
