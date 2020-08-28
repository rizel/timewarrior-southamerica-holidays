#!/usr/bin/python3.6.0
# -*- coding: utf-8 -*-

''' 
This python script extracts bolivian dates holidays
from this site https://publicholidays.com.bo/es/
so to be used with timewarrior.

USAGE:
$ python generate_southamerica_holidays.py bolivia 2020
'''

import sys
import requests
import io
import datetime
import time
import locale

from lxml import etree
from pathlib import Path
from pprint import pprint

countries = {
"argentina"           : ".com.ar",
"bolivia"             : ".com.bo",
"brasil"              : ".br.x", # http://www.public-holidays.us/BR_ES_2020_Feriados%20nacionais
"chile"               : ".cl",
"colombia"            : ".co",
"ecuador"             : ".la/ecuador",
"guayana"             : ".gy.x", #
"paraguay"            : ".com.py",
"peru"                : ".pe",
"surinam"             : ".sr.x", #
"trinidad y tobago"   : ".la/trinidad-and-tobago",
"uruguay"             : ".la/uruguay",
"venezuela"           : ".com.ve",
}



if __name__ == '__main__':
    country_name = sys.argv[1]
    string_year  = sys.argv[2]
    try:
        year = int(string_year)
        if (year<2020) or (year>2100):
            raise TypeError
        if country_name not in countries:
            raise NameError('Country data information not available.')

    except TypeError:
        print('Year value not allowed. Should be between 2020 and 2100.')
    except ValueError:
        print('Argument introduced is not a valid number for the year.')
    else:
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
        parser      = etree.HTMLParser(encoding='utf-8')
        country_code= countries[country_name]
        url         = f"https://publicholidays{country_code}/es/{year}-dates/"
        print(url)
        response    = requests.get(url)
        tree        = etree.parse(io.StringIO(response.text), parser)
        
        body_tag    = tree.find('body')
        table       = body_tag.xpath("//table[@class='publicholidays phgtable ']")
        table_content = table[0][1] # first element is header, second is table content.

        for tr_element in table_content[:-1]:
            attributes = tr_element.attrib
            # pprint(attributes)
            if (attributes):
                td_elements = tr_element.findall('td')
                date        = td_elements[0].text
                description = td_elements[2][0].text

                localed_date    = time.strptime(f'{date} {year}', '%d %B %Y')
                formatted_date  = time.strftime('%Y_%m_%d', localed_date)
                print(f"{formatted_date} = {description}")
