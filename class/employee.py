#!/usr/bin/env python
class Employee:

	def __init__(self,fname,lname,salary):
		self.fname=fname
		self.lname=lname
		self.salary=salary
	
	def Fullname(self):
		return ("{} {}".format(self.fname,self.lname))

	

class Developer(Employee):
	def __init__(self,fname,lname,salary,progLang):
		super().__init__(fname,lname,salary)	
		self.progLang=progLang

class Manager(Employee):
	def __init__(self,fname,lname,salary,employees=None):
		super().__init__(fname,lname,salary)
		if employees is None:
			self.employees=[]
		else:
			self.employees=employees
	def addEmp(self,emp):
		if emp in self.employees:
			self.employees.append(emp)
			
	def delEmp(self,emp):
		if emp in self.employees:
			self.employees.remove(emp)
	def printEmp(self):
		for emp in self.employees:
			print emp.Fullname

newEmp1 = Developer("sameer","gawande",10000,"python")
newMan = Manager("anjana","deepak",24000,[newEmp1])
print newMan.salary

print newEmp1.fname
print newEmp1.lname
print newEmp1.progLang
print newEmp1.concatName()

