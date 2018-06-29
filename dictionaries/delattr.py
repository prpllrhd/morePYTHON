#!/usr/bin/env python
class foo():
    def __delattr__(self, name):
        print(name)
        super().__delattr__(name)

