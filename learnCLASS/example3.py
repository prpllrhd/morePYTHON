#!/usr/bin/env python
import hostlists
'''
step 1
define a class Employee 
define 3 variables, fname,lname,salary
create email from fname+lname@co.com
write a function to print fname+lname
write a function to define a raise
'''
class employee():
	no_of_emp = 0
	raise_amount = 1.10
	def __init__(self,fname,lname,pay):
		self.fname = fname
		self.lname = lname
		self.pay = pay
		self.email = fname+"."+lname+"@company.com"
		employee.no_of_emp+=1
	def print_fullname(self):
		return ('{} {}'.format(self.fname,self.lname))
	def get_raise(self):
		self.pay = int(self.pay*employee.raise_amount)
	def print_sal(self):
		return '{}'.format(self.pay)
class hosts(object):
	def __init__(self,nodes):
		self.nodes = nodes
	def convertcurly(self):
		if "{" in self.nodes:
			self.nodes = self.nodes.replace("{","[")
			self.nodes = self.nodes.replace("}","]")
			self.nodes = self.nodes.replace("..","-")
			
		return hostlists.expand(self.nodes)



