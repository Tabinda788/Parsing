import csv
import requests
import xml.etree.ElementTree as ET
from csv import writer
import os

tree = ET.parse('clinical_study1.xml')
root = tree.getroot()

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
# print(adress)
city = adress[0][0].text
country_and_zip = adress[0][1].text

p = 0 
for i in adress:
    # print(i)
    l = []
    city = adress[p][0].text
    l.append(city)
    try:
        zip_code = adress[p][2].text
        l.append(zip_code)
    except:
        zip_code = None
        
    country = adress[p][1].text
    l.append(country)
    text_strings = ','.join(map(str, l))


    print(text_strings)
    p = p + 1

# site_addresses = tree.findall("./location/facility/address/city")
# print(site_addresses)
# site_addresses1 = tree.findall("./location/facility/address/country")
# print(site_addresses1)
# site_addresses2 = tree.findall("./location/facility/address/zip")
# print(site_addresses2)

# Innsbruck, Austria|Paris, France|Naarden, Netherlands - 1411 GE|Naarden, Netherlands - GE

# print(site_addresses[0].text)
# print(site_addresses1[0].text)
# print(site_addresses2[0].text)



def get_text(tag):
    index = 0
    text_list = []
    for text in tag:
        text = tag[index].text
        # print(text)
        text_list.append(text)
        index = index + 1
        text_strings = '|'.join(map(str, text_list))
    return text_strings


nct = get_text(nct_id)
# print(nct)
title = get_text(brief_title)
# print(title)
summary = get_text(brief_summary)
# print(summary)
description = get_text(detailed_description)
# print(description)
type_of_study=get_text(study_type)
# print(type_of_study)
criteria = get_text(eligibility_criteria)
# print(criteria)
condition = get_text(conditions)

intervention = get_text(interventions)
# print(intervention)

sponsers = get_text(lead_sponsor_name)
# print(sponsers)

names = get_text(site_names)
print(names)


