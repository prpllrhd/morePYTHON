#!/usr/bin/env python
import intspan
import re
def derangify(nodes):
    data_array = []
    for node in nodes:
        match = re.match('(.*)\[(.*)\](\..*)', node)
        if match:
            (prefix,nrange,suffix) = match.groups()
            length = 0
            for num in intspan(nrange):
                if length < len(str(num)): length = len(str(num))
            for num in intspan(nrange):
                data_array.append("%s%s%s" %(prefix,str(num).zfill(length),suffix))
        else:
            data_array.append(node)

    return data_array

def main():
  print derangify("gsrd111n[00-39].red.ygrid.yahoo.com")


if __name__=="__main__":
  main()
