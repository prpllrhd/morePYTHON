#!/usr/bin/env python
'''
give a host to be pinged and if the ping test failed, it logs the host
give a range of hosts and if the ping test failed for certain threshold, it logs the failed hosts
'''
from fabric.api import *
import argparse,hostlists,logging,subprocess
parser = argparse.ArgumentParser()
parser.add_argument('-ho','--host')
parser.add_argument('-hs','--hosts')
args = parser.parse_args()
logger = logging.getLogger("mylogger")
logging.basicConfig(level=logging.ERROR)
from logging.handlers import SMTPHandler
mail_handler = SMTPHandler(mailhost='smarthost.yahoo.com',fromaddr='samy@yahoo-inc.com',toaddrs=['samy@yahoo-inc.com'], subject='YourApplication Failed')
mail_handler.setLevel(logging.ERROR)

def pingtest(h):
  success = list()
  fail = list()
  #with settings(warn_only=True):
  #with settings(hide('stderr', 'warnings','stdout'),warn_only=True):
  with settings(hide('everything'),warn_only=True):
    nodes = hostlists.expand(h)
    for each in nodes:
      result = local("ping -c1 "+each)
      if result.return_code == 0:
        success.append(each)
      else:
        fail.append(each)
    logging.error(fail)
    logging.error(success)
    logger.addHandler(mail_handler)
    print "success:",len(success),success,"failed:",len(fail),fail

if args.hosts:
  no = args.hosts
elif args.host:
  no = args.host
pingtest(no)

def main():
  if __name__ == "__main__":
    main()
