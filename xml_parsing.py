#Python code to illustrate parsing of XML files
# importing the required modules
import csv
import requests
import xml.etree.ElementTree as ET
from csv import writer
tree = ET.parse('SearchResults.xml')
root = tree.getroot()
headerList = ['Status','Study Title','Conditions', 'Interventions', 'Locations']
with open("trials.csv", 'w') as file:
	dw = csv.DictWriter(file, delimiter=',', 
						fieldnames=headerList)
	dw.writeheader()


def total_child():
	total_roots = root.attrib
	count = total_roots['count']
	count = int(count) + 1
	return count

def write_to_csv(data):
	with open(data, 'a') as f_object:
		writer_object = writer(f_object)
		writer_object.writerow(row)
	return data


def extract_data(index):
	index_count = 0
	text_list = []
	for j in root[i][index]:
		text = root[i][index][index_count].text
		text_list.append(text)
		index_count= index_count+1
	text_strings = ','.join(map(str, text_list))
	return text_strings

iter = total_child()
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
		conditions= extract_data(3)
		row.append(conditions)
	except IndexError as error:
		conditions = None
		row.append(conditions)
	try:
		inventions= extract_data(4)
		row.append(inventions)

	except IndexError as error:
		inventions = None
		row.append(inventions)
	try:
		locations = extract_data(5)
		row.append(locations)
	except IndexError as error:
		locations = None
		row.append(locations)
	add_csv =  write_to_csv('trials.csv')	




