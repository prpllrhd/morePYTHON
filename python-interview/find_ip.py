#!/usr/bin/env python
import re
f = open("ip.txt")
findip = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",re.MULTILINE)
dict = {}
for i in f:
  ip=re.findall(findip,i)
  if dict.has_key(ip):
    dict[ip]+=1
  else:
    dict[ip]=1
print dict     
   
