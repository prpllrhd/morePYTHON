#!/usr/bin/env python
a=(line.strip() for line in open("/etc/passwd"))
b=[i for i in a]
print b
