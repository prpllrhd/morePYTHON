#!/usr/bin/env python2.7
#import hostlists
from fabric.api import *
env.debug=False
env.warnings=False
env.status=False
env.password="changeme"
env.disable_known_hosts=True
env.always_use_pty=False
env.roledefs = {
    'web': ['www1', 'www2', 'www3'],
    'dns': ['ns1', 'ns2']
}
#env.fabric.state.output=False
@task
@runs_once
def getUser():
	with hide('running'):
		print "this is being run by {}".format(env.user)
		execute(getCWD)
def getCWD():
	with hide('running'):
		env.cwd = "/tmp"
		print "the cwd  is {}".format(env.cwd)
@task
def runCMD(cmd):
	with hide('running'):
		run(cmd)

#@task
#def defineHosts(hostlist):
#	env.hosts = hostlists.expand(hostlist)
#	print env.hosts
@task
def putFile():
	with hide('running'):
		put("/Users/samy/git/python/iterdict.py","/home/samy/iterdict.py",mode=755)
#@task
#def runExternal():
#	run("/home/samy/iterdict.py")

@task
def runExternal():
	run("df")

@task
def getcurrhost():
	with hide('running'):
		print "current host is {}".format(env.host_string)
