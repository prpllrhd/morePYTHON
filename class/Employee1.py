#!/usr/bin/env python
class employee:
	bonus = 1.03
	emp_count = 0
	def __init__(self,fname,lname,sal):
		self.fname=fname
		self.lname=lname
		self.sal=sal
		self.email=self.fname+"_"+self.lname+"\@"+"company.com"
		employee.emp_count += 1

	def getSal( eachEmp ):
    		return eachEmp.sal
	
	def printempdetails(self):
		return '{}  {} has a salary of {}'.format(self.fname,self.lname,self.sal)
	
	def get_salary(self):
		self.sal = int(self.sal * self.bonus)
new_emp = employee("sameer","gawande",50000)
new_emp1 = employee("yuvi","gawande",80000)
new_emp2 = employee("rakhee","gawande",80000)
new_emp3 = employee("lata","gawande",180000)
print new_emp.printempdetails()
new_emp.get_salary()
print new_emp.printempdetails()
print employee.emp_count
#print employee.getMaxSal()
