#!/usr/bin/python3.6.0
# -*- coding: utf-8 -*-

''' 
This python script extracts dates holidays
from public holidays's sites like: 
  https://publicholidays.com.bo/es/
so to be used with timewarrior.

USAGE:
$ python generate_southamerica_holidays.py bolivia 2020

AUTHOR:
Lizbeth a.k.a. Rizel
'''

import sys

from extractor import extract_and_write_for
from countries import COUNTRIES


if __name__ == '__main__':
    country_name = sys.argv[1]
    string_year  = sys.argv[2]
    try:
        year = int(string_year)
        if (year<2020) or (year>2100):
            raise TypeError
        if country_name not in COUNTRIES:
            raise NameError('Country data information not available.')

    except TypeError:
        print('Year value not allowed. Should be between 2020 and 2100.')
    except ValueError:
        print('Argument introduced is not a valid number for the year.')
    else:
        extract_and_write_for(country_name, year)


