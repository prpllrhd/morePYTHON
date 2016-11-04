#!/usr/bin/env python
import argparse,hostlists
parser=argparse.ArgumentParser()
parser.add_argument("--hosts",nargs='+')
args=parser.parse_args()

class expandhosts:
  def __init__(self,hosts): 
    self.hosts=args.hosts

  def converttocomma(self):
    hl=[]
    hl=hostlists.expand(self.hosts)
    print ', '.join(hl)

  def converttonewline(self):
    hl=[]
    hl=hostlists.expand(self.hosts)
    print '\n'.join(hl)
    

def main():
  instance=expandhosts(args.hosts)
  
  instance.converttonewline()


if __name__=="__main__":
  main()
  
