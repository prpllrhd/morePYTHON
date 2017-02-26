#!/usr/bin/env python
import argparse,os
parser = argparse.ArgumentParser()
parser.add_argument("-v","--verbose",action='store_true')
args = parser.parse_args()
if args.verbose:
  print "Verbosity turned on"
#if args.verbose:
#  print os.listdir(".")
