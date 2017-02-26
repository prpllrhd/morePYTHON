#!/usr/bin/env python
class Emp:
#  var = []
  def __init__(self,val1,val2):
    self.val1 = val1
    self.val2 = val2
    self.var = []
  
  def appval(self,var):
    self.var.append(var)

a = Emp(1,2)
b = Emp(10,20)

a.appval(3)
b.appval(6)
b.appval(9)

print b.var
