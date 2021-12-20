import json
import csv
import glob
import os

dictionary2 = {}
empty_dictionary = {}

def add_key_value(dictionary, key, value):
    dictionary[key] = value
    return dictionary


def Merge(dict1, dict2):
    dict2.update(dict1)
    return dict2

def replace_split(labels):
    labels = labels[1:-1]
    labels = labels.replace("'","")
    labels = list(labels.split(","))
    return labels



def make_dictionaries(label_bucket_type):
    dictionary3 = dict()
    dictionary2['label_bucket_type'] = dictionary3
    dictionary4 = dict()
    label = rows['label']
    add_key_value(dictionary3,label,dictionary4)
    label_cui =  rows['label_cui']
    cui_label = replace_split(label_cui)
    dictionary4['cui'] = cui_label
    dictionary4['score'] = rows['label_score']
    dictionary4['label_semantic_types'] = rows['label_semantic_types']
    dictionary4['label_ncts_counts'] = rows['label_ncts_count']
    label_ncts = rows['label_ncts']
    ncts_label = replace_split(label_ncts)
    dictionary4['ncts'] = ncts_label
    empty_dictionary.setdefault(label_bucket_type,{})[label] = dictionary4
    return True
path = "/home/tabinda/Desktop/XML_Parsing/csvs"
csv_files = glob.glob(os.path.join(path, "*.csv"))

dumping_list = []
for file in csv_files:
    csvFilePath = file
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        some = list(csvReader)[0]
        first = list(some.values())[0]
        second = list(some.values())[1]
        # print(first, second)

    def form_final_dictionary():
        dictionary1 = {}
        dictionary1[first] = {"cui" : second}    
        value1 = dictionary1[first]
        merged = Merge(empty_dictionary,value1)
        final_dictionary = {}
        final_dictionary[first] = merged
        return final_dictionary

    csvFilePath = file
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:        
            if rows['label_bucket'] == 'have_had':
                bucket = rows['label_bucket']
                have_inserted = make_dictionaries(bucket)
            else:
                bucket = rows['label_bucket']
                look_inserted = make_dictionaries(bucket)   

    final = form_final_dictionary()
    dumping_list.append(final)

jsonFilePath = "/home/tabinda/Desktop/XML_Parsing/disease.json"
with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(dumping_list))