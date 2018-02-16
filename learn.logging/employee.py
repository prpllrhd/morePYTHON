#!/usr/bin/env python
import logging
logging.basicConfig(filename="employee.log",level=logging.INFO,
	format="%(asctime)s:%(levelno)s:%(message)s")
class Employee():
	def __init__(self,fname,lname):
		self.fname=fname
		self.lname=lname

		logging.info("Employee {} {} created".format(self.fname,self.lname))

emp_1 = Employee("sameer","gawande")
emp_2 = Employee("rakhee","gawande")
