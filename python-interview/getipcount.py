#!/usr/bin/env python
import re
ipdict={}
f=open("access.log")
comp=re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",re.M)
for i in f:
  a=re.search(comp,i)
  if ipdict.has_key(a.group()):
    ipdict[a.group()]+=1
  else:
    ipdict[a.group()]=1
print ipdict
