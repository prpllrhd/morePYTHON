#!/usr/bin/env python
import logging
logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter=logging.Formatter('%(asctime)s:%(message)s')
file_handler = logging.FileHandler("employee.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class Employee:
	def __init__(self,fname,lname,salary):
		self.fname=fname
		self.lname=lname
		self.salary=salary
		logger.debug("Employee with name {} {} and salary {} has been created".format(self.fname,self.lname,self.salary))

emp1 = Employee("sameer","gawande",89000)
emp2 = Employee("rakhee","gawande",19000)
emp3 = Employee("puru","kumar",99000)
		
