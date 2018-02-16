#!/usr/bin/env python
##dump xml file
import xml.etree.ElementTree as ET
tree = ET.parse('local-capacity-scheduler.xml')
root = tree.getroot()
print ET.dump(root)
