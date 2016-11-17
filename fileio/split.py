#!/usr/bin/env python
##to print specific columns from a file as keys in a dictionary
dict={}
f=(line.strip() for line in open("passwd"))
mylist=[tuple(i.split(":")) for i in f]
for each in mylist:
  dict.setdefault(each[0],[]).append(each[1])
  dict.setdefault(each[0],[]).append(each[3])
  dict.setdefault(each[0],[]).append(each[5])
print dict

