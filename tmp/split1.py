#!/usr/bin/env python
i=[line.strip() for line in open("/etc/passwd")]
mylist=[tuple(a.split(":")) for a in i]
print mylist
