#!/usr/bin/env python
import re
f=open("ip.txt")
line = " "
for i in f:
  line+=i
print line
b=re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
c=re.findall(b,line)
d=re.search(b,line)
print d.group()
#print c
#f.close()
  
