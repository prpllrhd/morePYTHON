#!/usr/bin/env python
import json
book={}
book['tom']={"name":"bob","age":41,"sex":"male"}
book["john"]={"name":"john","age":38,"sex":"male"}
s=json.dumps(book)

with open("file.json","w") as jsonfile:
  jsonfile.write(s)
