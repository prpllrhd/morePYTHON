#!/usr/bin/env python
dict={}
f=open("/etc/passwd")
rlines=[i for i.split(":") in f]
for each in rlines:
  if dict.has_key(each[-1]):
    dict[each]+=1
  else:
    dict[each]=1
print dict
