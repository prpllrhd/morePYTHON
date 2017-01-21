#!/usr/bin/env python
import logging

###create an object###
logger = logging.getLogger(__name__)

###set up the log level###
logger.setLevel(logging.INFO)	

###set up a filehandle where the logs would get written###
handler = logging.FileHandler('hello.log')

###set up log level for the file handle###
#handler.setLevel(logging.INFO)

###defining formatting###
logging.formatter = handler.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

###setting up defined formatting###
handler.setFormatter(formatter)

###add the handler to logger###
logger.addHandler(handler)

###finally w
logger.info('hello baby')
