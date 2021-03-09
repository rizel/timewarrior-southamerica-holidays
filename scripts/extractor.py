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

def data_extraction(country_name, year, tree):
    body_tag    = tree.find('body')
    table       = body_tag.xpath("//table[@class='publicholidays phgtable ']")
    table_content = table[0][1] # first element is header, second is table content. # tbody
   
    for tr_element in table_content[:-1]:
        attributes = tr_element.attrib
        pprint(attributes)
        if (attributes):
            td_elements = tr_element.findall('td')
            date        = td_elements[0].text
            description = td_elements[2][0].text

            localed_date    = time.strptime(f'{date} {year}', '%d %B %Y')
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



def url_for_country(country_name, year):
    country_code = COUNTRIES[country_name]
    if country_code.startswith('http:'):
        return country_code.format(year)
    return f"https://publicholidays{country_code}/es/{year}-dates/"


def extract_and_write_for(country_name, year):
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    parser      = etree.HTMLParser(encoding='utf-8')
    url         = url_for_country(country_name, year)
    print(url)
    response    = requests.get(url)
    tree        = etree.parse(io.StringIO(response.text), parser)

    special_data_extraction(country_name, year, tree)