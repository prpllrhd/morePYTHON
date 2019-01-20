#!/usr/bin/env python3
def compact(iterables):
	dedupes = []
	previous = object()
	for i in iterables:
		if i != previous:
			dedupes.append(i)
			previous = i
	return dedupes
		
#print compact([1,1,1,1,1,2,2,3,4,5,6,7,8,8,1,2])
print compact([])
