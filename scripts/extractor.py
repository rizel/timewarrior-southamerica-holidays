#!/usr/bin/python3.6.0
# -*- coding: utf-8 -*-

import requests
import io
import datetime
import time
import locale

from lxml import etree
from pathlib import Path
from pprint import pprint

from countries import COUNTRIES
from countries import ENGLISH_CONTENTS

def data_extraction(country_name, year, tree, input_date_format='%d %B %Y'):
    body_tag    = tree.find('body')
    table       = body_tag.xpath("//table[@class='publicholidays phgtable ']")
    table_content = table[0][1] # first element is header, second is table content. # tbody
   
    for tr_element in table_content[:-1]:
        attributes = tr_element.attrib
        # pprint(attributes)
        if (attributes):
            td_elements = tr_element.findall('td')
            date        = td_elements[0].text
            description = td_elements[2][0].text

            localed_date    = time.strptime(f'{date} {year}', input_date_format)
            formatted_date  = time.strftime('%Y_%m_%d', localed_date)
            print(f"{formatted_date} = {description}")


def special_data_extraction(country_name, year, tree):
    if country_name == 'brasil':
        body_tag        = tree.find('body')
        table           = body_tag.xpath("//table")
        table_content   = table[0][1]

        for tr_element in table_content[:]:
            td_elements = tr_element.findall('td')
            date        = td_elements[1].text
            description = td_elements[2].text

            localed_date    = time.strptime(f'{date}', '%A, %d %B %Y')
            formatted_date  = time.strftime('%Y_%m_%d', localed_date)
            print(f"{formatted_date} = {description}")
    elif (country_name in ENGLISH_CONTENTS):
        data_extraction(country_name, year, tree, '%d %b %Y')


def url_for_country(country_name, year):
    country_code = COUNTRIES[country_name]
    if (country_name == 'brasil'): 
        return country_code.format(year)
    if (country_name in ENGLISH_CONTENTS):
        return f"https://publicholidays{country_code}/{year}-dates/" 
    return f"https://publicholidays{country_code}/es/{year}-dates/"


def extract_and_write_for(country_name, year):
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    parser      = etree.HTMLParser(encoding='utf-8')
    url         = url_for_country(country_name, year)
    response    = requests.get(url)
    tree        = etree.parse(io.StringIO(response.text), parser)
    print(url)

    if (country_name == 'brasil'):
        special_data_extraction(country_name, year, tree)
    elif (country_name in ENGLISH_CONTENTS):
        locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
        special_data_extraction(country_name, year, tree)
    else:
        data_extraction(country_name, year, tree)
