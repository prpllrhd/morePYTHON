#!/usr/bin/env python
import csv
with open("mycsvfile.csv") as csv_file:
	csv_reader=csv.reader(csv_file)
	with open("newmycsvfile.csv","w") as newcsv_file:
		csv_writer = csv.writer(newcsv_file,delimiter="\t")
		for line in csv_reader:
			csv_writer.writerow(line)

