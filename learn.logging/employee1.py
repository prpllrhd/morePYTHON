#!/usr/bin/env python
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler=logging.FileHandler("employee1.log")
logger.addHandler(file_handler)

#logger.addHandler(logging.FileHandler("employee.log"))
formatter = logging.Formatter("%(asctime)s:%(levelno)s:%(message)s")
file_handler.setFormatter(formatter)
class Employee():
	def __init__(self,fname,lname):
		self.fname=fname
		self.lname=lname

		logger.info("Employee {} {} created".format(self.fname,self.lname))

emp_1 = Employee("ravi","shende")
emp_2 = Employee("mandar","nalawade")
