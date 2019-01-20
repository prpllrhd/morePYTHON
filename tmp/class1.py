#!/usr/bin/env python3
class Test:
	def f(self):
		return "Hello World!"

x = Test()
xf = x.f
print xf()
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
