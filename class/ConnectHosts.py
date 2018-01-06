#!/usr/bin/env python
from ExCLhostl import Hosts
import argparse
from fabric.api import *
def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--host")
  args = parser.parse_args()
  ho = Hosts(args.host)
  env.hosts = ho.expand()
  runCMD()
#def getHosts(nodes):
#  ho = Hosts(nodes)
#  return ho.expand()
def runCMD():
  with settings(hide('everything'),warn_only=True):
#      local("ping -c1 "+each)
      sudo("df")

if __name__ == "__main__":
  main()
