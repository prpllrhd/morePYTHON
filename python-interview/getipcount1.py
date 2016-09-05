#!/usr/bin/env python
import re
f=open("access.log")
ipdict={}
fi=re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
for i in f:
  findip=re.findall(fi,i)
  for ea in findip:
    if ipdict.has_key(ea):
      ipdict[ea]+=1
    else:
      ipdict[ea]=1
print ipdict
  
