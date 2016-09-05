#!/usr/bin/env python
def readnremspaces(file):
  with open(file) as f:
    a=f.read()
    print "".join(a.split(" "))##it keeps the new line as it was
   # print "".join(a.split())  ##all lines gets merged into 1
def main():
  readnremspaces("small.txt")

if __name__=="__main__":
  main()
