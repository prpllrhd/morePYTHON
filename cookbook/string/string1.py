#!/usr/bin/env python3
"""
example: script that imports os module to print files in a directory and print only files ending with .py
"""
import os
def help():
	print(__doc__)
def script():
	files = os.listdir(".")
	if (name.endswith(".py") for name in files):
		print("python")
	else:
		print("No Python")
def main():
	script()
	help()

if __name__=="__main__":
	main()
