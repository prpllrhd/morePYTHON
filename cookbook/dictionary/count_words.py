#!/usr/bin/env python3
"""
counting occurence of words using python3.
starting python3, has_key() has been removed. so use "in dict:"
"""
def count_words(words):
	d = {}
	w = words.split()
	for each in w:
		if each in d.keys():
			d[each]+=1
		else:
			d[each]=1
	print (d)
count_words("this is my perspective of my values and the other values") 
