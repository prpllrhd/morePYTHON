#!/usr/bin/env python
class Generic(Exception):
	def __init__(self,message):
		self.message = message

def getOutput(mssg):
	try:
		if (mssg == "oops"):
			raise Generic("This is bad news. Seems like some kind of error")
		else:
			print "No errors. Pls continue"
	except Generic,e:
#		print ("BadNews",e.message)
		raise
getOutput("oops")
