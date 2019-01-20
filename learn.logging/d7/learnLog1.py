#!/usr/bin/env python
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(name)s:%(asctime)s:%(message)s')
file_handler = logging.FileHandler("file123.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
class Employee:
	def __init__(self,fname,lname):
		self.fname=fname
		self.lname=lname
		logger.warn("Employee {} {} created".format(self.fname,self.lname))


emp1 = Employee("ravi","gupta")
emp2 = Employee("avinash","mittal")
