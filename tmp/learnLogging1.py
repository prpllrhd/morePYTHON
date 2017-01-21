#!/usr/bin/env python
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.info('start reading database')
records = {'john': 55, 'tom': 66}
logger.debug('Records: {}'.format(records))
logger.info('Updating records...')
logger.info('finish updating records')
