#!/usr/bin/env python
def student_info(*courses,**details):
	print courses
	print details
c = ["english","hindi"]
d = {"name":"sameer","age":43}

student_info(*c,**d)
