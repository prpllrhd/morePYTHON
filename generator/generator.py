#!/usr/bin/env python
def firstn(n):
    num = 0
    while num < n:
        yield (num*num)

sum_of_first_n = firstn(100)
for a in sum_of_first_n:
  print a
