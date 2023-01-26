#Python code to illustrate parsing of XML files
# importing the required modules
import csv
import requests
import xml.etree.ElementTree as ET
from csv import writer
from Generictools.trials import *
tree = ET.parse('results.xml')
root = tree.getroot()
headerList = ['Status','Study Title','Conditions', 'Interventions', 'Locations']
with open("trials.csv", 'w') as file:
	dw = csv.DictWriter(file, delimiter=',', 
						fieldnames=headerList)
	dw.writeheader()

obj = Trial()
iter = obj.total_child()
print(iter)

for i in range(1,iter):
	row = []
	try:
		status = root[i][1].text
		row.append(status)
	except IndexError as error:
		status = None
		row.append(status)
	try:
		study_title = root[i][0].text
		row.append(study_title)
	except IndexError as error:
		study_title = None
		row.append(study_title)
	try:
		conditions= obj.extract_data(i,3)
		row.append(conditions)
	except IndexError as error:
		conditions = None
		row.append(conditions)
	try:
		inventions= obj.extract_data(i,4)
		row.append(inventions)

	except IndexError as error:
		inventions = None
		row.append(inventions)
	try:
		locations = obj.extract_data(i,5)
		row.append(locations)
	except IndexError as error:
		locations = None
		row.append(locations)
	add_csv =  obj.write_to_csv(row,'trials.csv')	