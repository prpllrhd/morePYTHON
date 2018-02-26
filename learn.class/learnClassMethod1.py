#!/usr/bin/env python
##alternative constructor
class Employee:
	def __init__(self,fname,lname):
		self.fname=fname
		self.lname=lname
		self.email=self.fname+"."+self.lname+"@email.org"

	@classmethod
	def from_getinstance(cls,empstr):
		(first_n,last_n)=empstr.split("-")
		return cls(first_n,last_n)

emp_1="sameer-gawande"
emp_2="rakhee-gawande"

emp1 = Employee.from_getinstance(emp_1)
emp2 = Employee.from_getinstance(emp_2)

print emp1.fname
print emp2.lname
