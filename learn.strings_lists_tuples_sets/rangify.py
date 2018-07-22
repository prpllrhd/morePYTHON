#!/usr/bin/env python3
"""
hosts=gsbl300n[00-39].blue.ygrid.yahoo.com
"""
import re
class ranged:
	def __init__(self,hosts):
		self.hosts=hosts

	def createrange(self):
		templist = []
		searchformula = re.compile(r"([a-zA-Z]+)(\d{1,})(\w)(\[|\{)(\d{1,})\-(\d{1,})(\]|\})(.*)")
		match = searchformula.match(self.hosts)
		r1 = int(match.group(5))
		r2 = int(match.group(6))
		for each in range(r1,r2+1):
			print ('{}{}{}{:02}{}'.format(match.group(1),match.group(2),match.group(3),each,match.group(8)))

num = ranged("gsbl300n{00-39}.blue.ygrid.yahoo.com")		
num.createrange()
	
