#!/usr/bin/env python
class Employee:
  def __init__(self,fname,lname,salary):
    self.fname = fname
    self.lname = lname
    self.salary = salary
    self.email = fname + "." + lname + "@company.com"
  def printEmpDet(self):
    return self.fname + " " + self.lname + " " + str(self.salary) + " " + self.email
 
emp1 = Employee("sameer","gawande",88)
print emp1.printEmpDet()
emp2 = Employee("ravi","chandra",78)
print emp2.printEmpDet()
class Man:
  pass
man1=Man()
print man1

