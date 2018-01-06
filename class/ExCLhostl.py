#!/usr/bin/env python
import hostlists
class Hosts:
  def __init__(self,hl):
    self.hl = hl
  def expand(self):
    return hostlists.expand(self.hl)
#a = Hosts("a[1-100]")
#print a.expand()

"""
in another script you would include as follows
from ExCLhostl import Hosts
myhosts = Hosts("a[1-30].corp.yahoo.com")
print myhosts.expand()
"""
