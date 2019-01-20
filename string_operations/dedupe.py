def dedupe(items):
	seen = set()
	for item in items:
		if item not in seen:
			yield item
			seen.add(item)

a=[1,2,3,4,56,3,2,5,3,4,5,2,4,6,7,4,2]
print list(dedupe(a))
