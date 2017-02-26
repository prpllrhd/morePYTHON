#!/usr/bin/env python
class Emp:
  def __init__(self,n1,n2):
    self.n1 = n1
    self.n2 = n2
    return sum(self.n1,self.n2)
a = Emp(2,5)
