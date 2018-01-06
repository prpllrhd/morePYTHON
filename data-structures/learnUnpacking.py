#!/usr/bin/env python
records = [("foo", 1,3),("bar","hello"),("foo",2,4), ]

def do_foo(x,y):
  print('foo',y,y)

def do_bar(s):
  print('bar','s')

for *args in records:
  if tag == 'foo':
    do_foo(*args)
  if tag == 'bar':
    do_bar(*args)
