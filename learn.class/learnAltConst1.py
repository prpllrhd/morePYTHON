#!/usr/bin/env python
import time
class getDate:
	def __init__(self):

		@classmethod
		def fromtimestamp(cls, t):
			y, m, d, hh, mm, ss, weekday, jday, dst = _time.localtime(t)
			return cls(y, m, d)

		@classmethod
		def today(cls):
			"Construct a date from time.time()."
			t = time.time()
			return cls.fromtimestamp(t)
