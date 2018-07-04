#!/usr/bin/env python3
from functools import reduce
a=[1,2,3,4,5,6,7,7,8]
sum = reduce(lambda x,y: x+y,a)
print (sum)
