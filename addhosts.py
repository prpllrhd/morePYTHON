#!/usr/bin/env python
import re,argparse
parser=argparse.ArgumentParser()
parser.add_argument("--hosts",nargs="+")
args=parser.parse_args()
##gsrd646n[00-39].red.ygrid.yahoo.com
a=[]
hostsre=re.compile(r"([a-z0-9]+)\[[0-9-]+\]+\.[a-z.]+")
for each in args.hosts:
#   mapred=open("mapred.include")
   a=re.findall(hostsre,each)
print a
