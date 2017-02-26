#!/usr/bin/env python
import logging, logging.handlers
log = logging.getLogger("mylogger")
log.setLevel(logging.DEBUG)
h2 = logging.handlers.SMTPHandler(mailhost='smarthost.yahoo.com',
                            fromaddr='samy@yahoo-inc.com',
                            toaddrs=['samy@yahoo-inc.com'],
                            subject='The log',
                    #3        credentials=('user','pwd'),
                            secure=None)
h2.setLevel(logging.INFO)
#h2.setFormatter(f)
log.addHandler(h2)

log.info("Did something")
log.info("Did something else")
log.info("This would send a third email. :-(")
