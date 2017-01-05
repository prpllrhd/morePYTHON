#!/usr/bin/env python
import sys
import argparse
a=input()
try:
  f = open("a")
  print f

except IOError:
  print "Try again"
