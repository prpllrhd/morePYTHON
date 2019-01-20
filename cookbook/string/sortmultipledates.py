#!/usr/bin/env python
import re
def sortdates(*dates):
	dateformat = []
	dateformula = re.compile(r'(\d\d)\/(\d\d)\/(\d\d\d\d)')
	mindateformula = re.compile(r'(\d\d\d\d)(\d\d)(\d\d)')
	for each in dates:
		dateformat.append(dateformula.sub(r'\3\2\1',each))
	mindate = int(min(dateformat))
	return mindateformula.sub(r'\3/\2/\1',str(mindate))

def main():
	print sortdates("01/02/2013","03/04/1993","04/02/2014","01/12/1991")

if __name__ == "__main__":
	main()
