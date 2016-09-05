#!/usr/bin/env python
def addnum(*num):
  for i in num:
    total=sum(i)
  return total
def main():
    sums=addnum(range(20))
    print sums
if __name__=="__main__":
  main()
