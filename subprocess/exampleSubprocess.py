#!/usr/bin/env python
import subprocess
def main():
  renfil("old.test.file","new")

def renfil(o,nn):
  a=o.split('.')
  fnn = nn + '.' + a[1] + '.' + a[2]
  subprocess.call(["mv", o , fnn])

if __name__ == "__main__":
  main()
  

