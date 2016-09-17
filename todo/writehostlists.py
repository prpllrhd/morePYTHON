#!/usr/bin/env python
import hostlists
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("--expand2comma")
parser.add_argument("--expand2line")
args=parser.parse_args()

def converttocoma(hostlist):
  fw=open("/tmp/hl-c","w")
  hostlist=args.expand2comma
  xl=[]
  xl=(hostlists.expand(hostlist))
  fw.write(', '.join(xl))
  fw.close()

def converttonewline(hostlist):
  fw=open("/tmp/hl-l","w")
  hostlist=args.expand2line
  xl=[]
  xl=(hostlists.expand(hostlist))
  fw.write('\n'.join(xl))
  print type('\n'.join(xl))

def main():
  if args.expand2comma:
    converttocoma(args.expand2comma)
  elif args.expand2line:
    converttonewline(args.expand2line)

if __name__=="__main__":
  main()
