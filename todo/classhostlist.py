#!/usr/bin/env python
import argparse,hostlists

class expandhosts:
  def __init__(self,name): 
    self.name=name

  def converttocomma(self):
    hl=[]
    hl=hostlists.expand(self.name)
    print ', '.join(hl)

  def converttonewline(self):
    hl=[]
    hl=hostlists.expand(self.name)
    print '\n'.join(hl)
    

def main():
  instance=expandhosts("abc[1-50].gq1.yahoo.com")
  
  instance.converttonewline()


if __name__=="__main__":
  main()
  
