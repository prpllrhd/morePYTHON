from fabric.api import run, env
env.warn_only = True
env.hosts = ['spedsaid.corp.gq1.yahoo.com']
command = "date"
x = run(command, capture=True)
print x.stdout
print x.stderr
