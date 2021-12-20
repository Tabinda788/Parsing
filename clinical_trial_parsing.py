import csv
import xml.etree.ElementTree as ET
from csv import writer
import os

path = "/home/tabinda/Desktop/XML/search_result"
headerList = ['nct_id', 'brief_title', 'brief_summary', 'detailed_description', 'study_type',
              'eligibility_criteria', 'conditions', 'interventions', 'lead_sponsor_name',
              'site_names', 'site_addresses']

with open("clinical_trials.csv", 'w') as file:
    dw = csv.DictWriter(file, delimiter=',',
                        fieldnames=headerList)
    dw.writeheader()


def write_to_csv(data):
    with open(data, 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(row)
    return data


def get_text(tag):
    text_strings = None
    index = 0
    text_list = []
    for text in tag:
        try:
            text = tag[index].text
            text = text.replace("\r", "")
            text = text.replace("\n", "")
            text_list.append(text.rstrip())
            index = index + 1
            text_strings = '|'.join(map(str, text_list))
        except:
            text = None
            text_list.append(text)
            index = index + 1
            text_strings = '|'.join(map(str, text_list))
            return text_strings
    return text_strings


def get_adress(adress, city, zip, country):
    list_strings = None
    address_index = 0
    adress_list = []
    for i in adress:
        l = []
        try:
            city_text = city[address_index].text
        except IndexError as error:
            city_text = ""
        try:
            country_text = country[address_index].text
        except IndexError as error:
            country_text = ""
        try:
            zip_text = zip[address_index].text
        except IndexError as error:
            zip_text = ""
        address_index = address_index + 1
        l.extend([city_text, country_text, zip_text])
        final_string = city_text + "," + country_text + "-" + zip_text
        adress_list.append(final_string)
        list_strings = '|'.join(map(str, adress_list))
    return list_strings


def get_memory_adress():
    nct_id = tree.findall("./id_info/nct_id")
    brief_title = tree.findall("./brief_title")
    brief_summary = tree.findall("./brief_summary/textblock")
    detailed_description = tree.findall("./detailed_description/textblock")
    study_type = tree.findall("./study_type")
    eligibility_criteria = tree.findall("./eligibility/criteria/textblock")
    conditions = tree.findall("./condition")
    interventions = tree.findall("./intervention/intervention_name")
    lead_sponsor_name = tree.findall("./sponsors/lead_sponsor/agency")
    site_names = tree.findall("./location/facility/name")
    adress = tree.findall("./location/facility/address")
    city = tree.findall("./location/facility/address/city")
    zip = tree.findall("./location/facility/address/zip")
    country = tree.findall("./location/facility/address/country")

    return nct_id, brief_title, brief_summary, detailed_description, study_type, \
        eligibility_criteria, conditions, interventions, lead_sponsor_name, \
        site_names, adress, city, zip, country


for filename in os.listdir(path):
    row = []
    if not filename.endswith('.xml'):
        continue
    fullname = os.path.join(path, filename)
    tree = ET.parse(fullname)
    id_adress, title_adress, summary_adress, description_adress, \
        study_type_adress, criteria_adress, condition_adress, interventions_adress, \
        sponsor_adress, names_adress, location_adress, location_city, \
        location_zip, location_country = get_memory_adress()
    nct = get_text(id_adress)
    title = get_text(title_adress)
    summary = get_text(summary_adress)
    description = get_text(description_adress)
    type_of_study = get_text(study_type_adress)
    criteria = get_text(criteria_adress)
    condition = get_text(condition_adress)
    intervention = get_text(interventions_adress)
    sponsers = get_text(sponsor_adress)
    names = get_text(names_adress)
    adres = get_adress(location_adress, location_city,
                       location_zip, location_country)
    # print(adres)

    row.extend([nct, title, summary, description, type_of_study, criteria, condition,
                intervention, sponsers, names, adres])
    write_to_csv("clinical_trials.csv")
