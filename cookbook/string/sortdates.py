#!/usr/bin/env python3
def sortdates(d1,d2):
	a1,a2,a3 = d1.split("/")
	dt1 = a2+a1+a3
	b1,b2,b3 = d2.split("/")
	dt2 = b2+b1+b3
	if dt1  > dt2 :
		return d1
	else:
		return d2
print sortdates("06/01/2017","04/03/2014")
	
