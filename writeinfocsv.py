#!/usr/bin/env python
wf = open('inputfile.csv', 'w')
rf = (line.strip() for line in open("info.csv"))
mylist=[tuple(i.split(',')) for i in rf]
for each in mylist:
	wf.write("edit "+each[0]+"\n"+"set associated-interface \"trust\"\n"+"set subnet "+each[1]+" "+each[2]+"\n"+"next\n")
wf.close()
