import json
import csv
from csv import writer


def read_json(filename: str) -> dict:

    try:
        with open(filename, "r") as f:
            data = json.loads(f.read())
    except:
        raise Exception(f"Reading {filename} file encountered an error")

    return data


data = read_json(filename="disease.json")


def list_to_string(data):
    converted_list = ' '.join(map(str, data))
    return converted_list


headerList = ['disease', 'disease_cui', 'label', 'label_cui', 'score',
              'label_semantic_type', 'label_nct_count', 'label_nct', 'label bucket']
with open("new_data.csv", 'w') as file:
    dw = csv.DictWriter(file, delimiter=',',
                        fieldnames=headerList)
    dw.writeheader()


def retrieve_data(data):

    try:
        key = list(data.keys())[0]
        disease_data = data[empty_list[index]]
        have_had_key = list(disease_data.keys())[1]
        looking_for_key = list(disease_data.keys())[2]
        outer_cui = disease_data["cui"]
        have_had = disease_data["have_had"]
        looking_for = disease_data["looking_for"]
        intraocular_lens_implantation = have_had["intraocular lens implantation"]
        inner_cui = intraocular_lens_implantation["cui"]
        score = intraocular_lens_implantation["score"]

        return key, have_had_key, looking_for_key, outer_cui, have_had, looking_for

    except:
        raise Exception(f"Error in retrieving data from json data file")


def insert_rows():

    try:
        for k, v in have_had_dictionary.items():
            have_lis = []
            have_lis.append(disease)
            have_lis.append(disease_cui)
            have_lis.append(k)
            for a in v.values():
                if isinstance(a, list):
                    have_string = list_to_string(a)
                    have_lis.append(have_string)
                else:
                    have_lis.append(a)
            have_lis.append(have)
            with open('new_data.csv', 'a') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(have_lis)

        for m, n in looking_for_dictionary.items():
            look_lis = []
            look_lis.append(disease)
            look_lis.append(disease_cui)
            look_lis.append(m)
            for c in n.values():
                if isinstance(c, list):
                    look_string = list_to_string(c)
                    look_lis.append(look_string)
                else:
                    look_lis.append(c)
            look_lis.append(looking)
            with open('new_data.csv', 'a') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(look_lis)
        return True
    except:

        raise Exception(f"Error in inserting rows in csv")


index = 0
for disease in data:
    empty_list = []
    for key, value in disease.items():
        empty_list.append(key)
    # print(empty_list[index])

    def write_to_file(data: str, filepath: str) -> bool:

        try:
            with open(filepath, "w+") as f:
                f.write(data)
        except:
            raise Exception(f"Saving data to {filepath} encountered an error")

    disease, have, looking, disease_cui, have_had_dictionary, looking_for_dictionary = \
        retrieve_data(disease)

    is_inserted = insert_rows()
    if is_inserted == True:
        print("Csv %s Data inserted" % str(empty_list[0]))
