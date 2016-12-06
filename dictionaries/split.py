#!/usr/bin/env python
##to print specific columns from a file as keys in a dictionary
dict={}
f=(line.strip() for line in open("all"))
mylist=[tuple(i.split(" ")) for i in f]
for each in mylist:
  dict.setdefault(each[1],[]).append(each[2])
  dict.setdefault(each[1],[]).append(each[3])
  dict.setdefault(each[1],[]).append(each[5])
print dict['19']
