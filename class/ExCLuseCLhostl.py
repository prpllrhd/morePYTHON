#!/usr/bin/env python
from ExCLhostl import Hosts
from fabric.api import sudo
host = Hosts("abc[1-100].corp.yahoo.com")
print host.expand()
def runCMD(h):
  for each in h:
    print each
runCMD(host)
    

