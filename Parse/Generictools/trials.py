import csv
import requests
import xml.etree.ElementTree as ET
from csv import writer
tree = ET.parse('results.xml')
root = tree.getroot()


class Trial:
    def total_child(self):
        total_roots = root.attrib
        count = total_roots['count']
        count = int(count) + 1
        return count

    def write_to_csv(self,row,data):
        with open(data, 'a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(row)
        return data

    def extract_data(self,i,index):
        index_count = 0
        text_list = []
        for j in root[i][index]:
            text = root[i][index][index_count].text
            text_list.append(text)
            index_count= index_count+1
        text_strings = ','.join(map(str, text_list))
        return text_strings
