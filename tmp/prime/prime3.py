#!/usr/bin/env python
num=143
for i in range(2,num):
  if num%i==0:
     prime=False
  else:
     prime=True
if prime==True:
  print num
