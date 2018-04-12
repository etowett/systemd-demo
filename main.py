#!/usr/bin/env python

import time
import sys
import logging
import logging.config

logging.config.fileConfig('logging.ini')
logger = logging.getLogger('complex')


def do_complex_stuff(arg):
    logger.info("working on stuff. Given arg: %s" % arg)
    logger.error("This is if an error")
    return


if __name__ == '__main__':
    while True:
        try:
            arg = sys.argv[1]
        except Exception:
            arg = None
        do_complex_stuff(arg)
        time.sleep(5)
