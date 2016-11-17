lnum=input("enter low num\n")
hnum=input("enter high num\n")
print type(lnum)
print type(hnum)

for i in range(lnum,hnum):
  prime=True
  for j in range((lnum+1),hnum):
     if i%j==0:
        prime=False
  if prime==True:
     print i

