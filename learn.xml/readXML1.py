#!/usr/bin/env python
##read a xml file and print it
import xml.etree.ElementTree as ET
tree = ET.parse('local-capacity-scheduler.xml')
root = tree.getroot()
for child in root.iter():
	print child.tag,child.text

