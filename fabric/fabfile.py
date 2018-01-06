#!/usr/local/bin/env python2.7
from fabric.api import run
def getOS():
	run('uname -a')

