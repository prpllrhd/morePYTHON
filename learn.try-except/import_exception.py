class Error(Exception):
	
	def __init__(self,value):
		self.value = value

	def  __str__(self):
		return (repr(self.value))

try:
	raise(Error(3**2))
except Error as error:
	print ("A new exception occured",error.value)
