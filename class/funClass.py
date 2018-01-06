#!/usr/bin/env python
# Define a function `plus()`
#def plus(a,b):
#  return a + b
  
class Summation:
  def __init__(self, a, b):
    self.a=a
    self.b=b
    content = self.a + self.b
#    print content
  def printval(self):
    return "the sum of {} and {} is {}".format(self.a,self.b,self.a+self.b)
o = Summation(12,23)
print o.printval()
Summation(13,456)


