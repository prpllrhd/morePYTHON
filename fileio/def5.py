dict={}
f=(line.strip() for line in open("/etc/passwd"))
mylist=[tuple(i.split(":")) for i in f]
for each in mylist:
  dict.setdefault(each[0],[]).append(each)
#  dict.setdefault(each[0],[]).append(each[3])
#  dict.setdefault(each[0],[]).append(each[6])
for i in dict.items():
  print i

