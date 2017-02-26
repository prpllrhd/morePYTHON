import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--verbose",action="store_true")
parser.add_argument("--another")
args = parser.parse_args()
print type(args)
if args.verbose:
  print "verbocity triggererd"
