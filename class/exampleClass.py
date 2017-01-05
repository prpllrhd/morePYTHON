#!/usr/bin/env python
class Emp:
  def __init__(self,name,age):
    self.name = name
    self.age = age
p1 = Emp("sameer",41)
print "the name is {0.name} and his age is {0.age}".format(p1)
