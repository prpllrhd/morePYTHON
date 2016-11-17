dict={}
#with open("/etc/passwd") as f:
f=(line.strip() for line in open("/etc/passwd"))
mylist=[tuple(i.split(':')) for i in f]
for each in mylist:
  dict.setdefault(each[0],[]).append(each[1:2])
for i in dict.items():
  print i
print dict
