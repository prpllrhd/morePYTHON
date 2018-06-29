#!/usr/bin/env python
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler=logging.FileHandler("kernelfix.log")
logger.addHandler(file_handler)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


