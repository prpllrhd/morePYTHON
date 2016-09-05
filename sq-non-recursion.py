#!/usr/bin/env python
def nonrecur(num,pow):
    a=num
    while pow > 0:
        num = num * a
        pow-=1
print nonrecur(4,5)
