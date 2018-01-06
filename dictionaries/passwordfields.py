#!/usr/bin/env python
a=(line.strip() for line in open("/etc/passwd"))
print "type a:",type(a)
b=[i for i in a]
print b
