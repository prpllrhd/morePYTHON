#!/usr/bin/env python3

"""open a file and read it and if the contents exists in another file, ignore those. if not exists, add the contents at the end of file  along with other contents."""

with open("readfile.txt","r") as fr:
	fread = fr.read()
	with open("readwritefile.txt","rw") as frw:
		for each in fread:
			if fread.findall(frw):
				pass
			else:
				frw.write(each)
		
