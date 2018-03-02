#!/usr/bin/env python
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("raiseE.txt")
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

stream_handler=logging.StreamHandler()
logger.addHandler(stream_handler)

class RaiseNewException(Exception):
	def __init__(self,message):
		self.message=message

def getMessage(msg):
	try:
		if msg == "oops":
			raise RaiseNewException("Arre kya kar diya")
		else:
			pass
	except RaiseNewException, e:
		logger.debug("BadNews {}".format(e.message))

def getNameError():
	try:
		a=sameer
	except NameError:
		logger.error("The variable is not defined")
	else:
		print "Man you passed it"
def kbError():
	while True:
		try:
			x = int(raw_input("Enter a number"))
			break
		except KeyboardInterrupt:
			print "KB errror, try again"
		except ValueError:
			print "incorrect value, try again"
	

def main():
	getMessage("oops")
	getNameError()
	kbError()

if __name__ == "__main__":
	main()
