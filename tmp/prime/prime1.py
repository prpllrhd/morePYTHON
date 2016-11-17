#!/usr/bin/env python
for i in range(1,101):
  prime=True
  for j in range(2,i):
    if i%j==0:
      prime=False
  if prime==True:
    print i
