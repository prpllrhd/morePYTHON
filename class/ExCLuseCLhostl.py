#!/usr/bin/env python
from ExCLhostl import Hosts
host = Hosts("abc[1-100].corp.yahoo.com")
print host.expand()

