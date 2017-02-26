#!/usr/bin/env python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square",type=int)
args = parser.parse_args()
if args.square:
  print args.square**2
