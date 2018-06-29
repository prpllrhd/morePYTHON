numbers = '''
408-349-2100
800 343 4422
888 342 4325
650.334.4563
708.655.7151
'''
names = '''
Sameer Gawande
Mr Ravi Arora
Mr. Ashwin Malhotra
Ms Puja Mehra
Mrs Suman Patra
'''

http://www.google.com
www.aol.com
www.verizon.com
uscis.gov
stanford.edu
www.oath.com
https://www.fbi.gov
www.irtc.com

duplicates = "he he is a boy boy but but he also get"
name = 'Sameer Gawande Mr Ravi Arora Mr. Ashwin Malhotra Mr. Ashwin Malhotra Ms Puja Mehra Mrs Suman Patra coreyms.com'

import re

#with open("textfile.txt","r") as file:
#	fh = file.read()
#	findnames = re.compile(r"(Mrs|Mr|Ms)\.?")
#	fname = findnames.findall(fh)
#	for each in fname:
#		print each
#	
#findnum = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')
#find = findnum.finditer(numbers)
#for each in find:
#	print each

#findnames = re.compile(r"(Mrs|Mr|Ms)\.?")
#findnames = re.compile(r".")
#findnames = re.compile(r"coreyms\.com")
#findnames = re.compile(r"\b[A-Z]\w*")
#fname = findnames.findall(name)
#for a in fname:
#        print a

#################numbers##################
###find phone number in any format eg: xxx xxx xxxx or xxx-xxx-xxxx or xxx.xxx.xxxx
#findnumber = re.compile(r'(\d{3}.\d{3}.\d{4})')

###find phone number in only 2 formats xxx-xxx-xxxx or xxx.xxx.xxxx and exclude xxx*xxx*xxxx and exclude xxx xxx xxxx
findnumber = re.compile(r"\d{3}[.-]\d{3}[.-]\d{4}")

###findall
searchnum = findnumber.findall(numbers)
for num in searchnum:
	print num

##finditer
#searchnum = findnumber.finditer(numbers)
#for num in searchnum:
#	print num.group(1)

##search
#searchnum = findnumber.search(numbers)
#print searchnum.group(1)

##match
#searchnum = findnumber.match(numbers)
#print searchnum
