#!/usr/bin/env python
import sys
"""Illustration of reraise an exception
"""


class MyCustomException(Exception):
	pass


def foo():
    a = 1
    b = 0
    return a / b


def bar():
    try:
        foo()
    except ZeroDivisionError as e:
        # we wrap it to our self-defined exception
        raise MyCustomException, MyCustomException(e), sys.exc_info()[2]


bar()

