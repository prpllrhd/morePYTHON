#!/usr/bin/env python
import logging
import os
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Starting")
a=os.uname()
logger.debug("uname done")
b=os.getcwd()
logger.info("cwd done")
