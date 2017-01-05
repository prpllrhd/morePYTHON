#!/usr/bin/env python
dict={}
f=(i.strip() for i in open("/etc/passwd"))
b = [j for j in f]
print b
#for each in rlines:
#  if dict.has_key(each[-1]):
#    dict[each]+=1
#  else:
#    dict[each]=1
#print dict
