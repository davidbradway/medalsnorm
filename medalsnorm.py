# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 08:51:40 2016

@author: dpb6
"""

# MEDALS
import os
import pickle
import sys
import numpy as np
import pandas as pd

from lightning import Lightning
from numpy import random

lgn = Lightning(ipython=True, host='http://public.lightning-viz.org')

countries = ['ISO', 'SLE', 'COD', 'CAF', 'TCD', 'AGO', 'GNB', 'GNQ', 'MLI',
             'MWI', 'BDI', 'NGA', 'SOM', 'SSD', 'MOZ', 'CIV', 'CMR', 'GIN',
             'BFA', 'AFG', 'ZMB', 'MRT', 'SWZ', 'LSO', 'TGO', 'BEN', 'COG',
             'COM', 'LBR', 'PAK', 'UGA', 'NER', 'DJI', 'YEM', 'TZA', 'GMB',
             'RWA', 'ETH', 'KEN', 'TJK', 'GHA', 'SEN', 'ERI', 'MMR', 'ZWE',
             'ZAF', 'GAB', 'KHM', 'TLS', 'IND', 'TKM', 'PNG', 'HTI', 'LAO',
             'UZB', 'STP', 'BOL', 'MDG', 'NPL', 'ESH', 'BGD', 'NAM', 'SLB',
             'AZE', 'BTN', 'KIR', 'BWA', 'KGZ', 'FSM', 'IRQ', 'MAR', 'PRY',
             'GUY', 'MNG', 'GTM', 'DZA', 'DOM', 'IDN', 'VUT', 'HND', 'PRK',
             'KAZ', 'TTO', 'JAM', 'BRA', 'EGY', 'PHL', 'WSM', 'PSE', 'SUR',
             'TON', 'GEO', 'CPV', 'NIC', 'ECU', 'ARM', 'PER', 'IRN', 'SLV',
             'JOR', 'COL', 'TUN', 'VCT', 'CHN', 'FJI', 'PAN', 'VEN', 'LBY',
             'MEX', 'TUR', 'ALB', 'ABW', 'VNM', 'BLZ', 'MDA', 'MDV', 'NCL',
             'SYR', 'GUF', 'SAU', 'ARG', 'MUS', 'URY', 'UKR', 'ROU', 'MKD',
             'LCA', 'THA', 'BRB', 'GUM', 'MNE', 'VIR', 'LKA', 'GRD', 'SYC',
             'BHS', 'ATG', 'LBN', 'CRI', 'BGR', 'OMN', 'KWT', 'BIH', 'PYF',
             'BHR', 'LVA', 'MTQ', 'QAT', 'CHL', 'PRI', 'GLP', 'ARE', 'USA',
             'BLR', 'SVK', 'POL', 'LTU', 'MLT', 'HRV', 'MYT', 'REU', 'HUN',
             'CAN', 'TWN', 'BRN', 'CUB', 'MAC', 'NZL', 'GBR', 'MYS', 'EST',
             'KOR', 'AUS', 'CYP', 'GRC', 'CHE', 'NLD', 'ISR', 'DNK', 'BEL',
             'AUT', 'IRL', 'DEU', 'FRA', 'ESP', 'ITA', 'PRT', 'CZE', 'NOR',
             'SVN', 'FIN', 'JPN', 'SWE', 'LUX', 'SGP', 'ISL', 'HKG', 'FLK',
             'SMR', 'TCA', 'VAT', 'RUS', 'GRL']

values = (random.rand(len(countries)) * 5).astype('int')
lgn.map(countries, values, colormap='Pastel1', width=900)

    # Dict of country codes
    codes = {'Afghanistan': 'AFG', 'Albania': 'ALB', 'Algeria': 'DZA',
             'American Samoa': 'ASM', 'Angola': 'AGO',
             'Antigua and Barbuda': 'ATG', 'Argentina': 'ARG',
             'Armenia': 'ARM', 'Aruba': 'ABW', 'Australia': 'AUS',
             'Austria': 'AUT', 'Azerbaijan': 'AZE', 'The Bahamas': 'BHS',
             'Bahrain': 'BHR', 'Bangladesh': 'BGD', 'Barbados': 'BRB',
             'Belarus': 'BLR', 'Belgium': 'BEL', 'Belize': 'BLZ',
             'Benin': 'BEN', 'Bermuda': 'BMU', 'Bhutan': 'BTN',
             'Bolivia': 'BOL', 'Bosnia & Herzegovina': 'BIH',
             'Botswana': 'BWA', 'Brazil': 'BRA', 'Brunei Darussalam': 'BRN',
             'Bulgaria': 'BGR', 'Burkina Faso': 'BFA', 'Burundi': 'BDI',
             'Cambodia': 'KHM', 'Cameroon': 'CMR', 'Canada': 'CAN',
             'Cape Verde': 'CPV', 'Central African Rep.': 'CAF', 'Chad': 'TCD',
             'Chile': 'CHL', 'China': 'CHN', 'Hong Kong': 'HKG',
             'Macao': 'MAC', 'Colombia': 'COL', 'Comoros': 'COM',
             'Democratic Republic of Congo': 'ZAR', 'Republic of Congo': 'COG',
             'Costa Rica': 'CRI', 'Côte d\'Ivoire': 'CIV', 'Croatia': 'HRV',
             'Cuba': 'CUB', 'Czech Republic': 'CZE', 'Denmark': 'DNK',
             'Djibouti': 'DJI', 'Dominica': 'DMA', 'Dominican Republic': 'DOM',
             'Ecuador': 'ECU', 'Egypt': 'EGY', 'El Salvador': 'SLV',
             'Equatorial Guinea': 'GNQ', 'Eritrea': 'ERI', 'Estonia': 'EST',
             'Ethiopia': 'ETH', 'Faeroe Islands': 'FRO', 'Fiji': 'FJI',
             'Finland': 'FIN', 'France': 'FRA', 'French Polynesia': 'PYF',
             'Gabon': 'GAB', 'The Gambia': 'GMB', 'Georgia': 'GEO',
             'Germany': 'DEU', 'Ghana': 'GHA', 'Gibraltar': 'GIB',
             'Greece': 'GRC', 'Greenland': 'GRL', 'Grenada': 'GRD',
             'Guadeloupe': 'GLP', 'Guam': 'GUM', 'Guatemala': 'GTM',
             'French Guiena': 'GUF', 'Guinea': 'GNB', 'Guinea-Bissau': 'GIN',
             'Guyana': 'GUY', 'Haiti': 'HTI', 'Honduras': 'HND',
             'Hungary': 'HUN', 'Iceland': 'ISL', 'India': 'IND',
             'Indonesia': 'IDN', 'Islamic Republic of Iran': 'IRN',
             'Iraq': 'IRQ', 'Ireland': 'IRL', 'Israel': 'ISR', 'Italy': 'ITA',
             'Jamaica': 'JAM', 'Japan': 'JPN', 'Jordan': 'JOR',
             'Kazakhstan': 'KAZ', 'Kenya': 'KEN', 'Kiribati': 'KIR',
             'South Korea': 'KOR', 'Kuwait': 'KWT', 'Kyrgyzstan': 'KGZ',
             'Lao People\'s Dem.Rep': 'LAO', 'Latvia': 'LVA', 'Lebanon': 'LBN',
             'Lesotho': 'LSO', 'Liberia': 'LBR', 'Libya': 'LBY',
             'Lithuania': 'LTU', 'Luxembourg': 'LUX', 'FYR Macedonia': 'MKD',
             'Madagascar': 'MDG', 'Malawi': 'MWI', 'Malaysia': 'MYS',
             'Maldives': 'MDV', 'Mali': 'MLI', 'Malta': 'MLT',
             'Martinique': 'MTQ', 'Mauritania': 'MRT', 'Mauritius': 'MUS',
             'Mexico': 'MEX', 'Moldova': 'MDA', 'Mongolia': 'MNG',
             'Morocco': 'MAR', 'Mozambique': 'MOZ', 'Myanmar': 'MMR',
             'Namibia': 'NAM', 'Nauru': 'NAU', 'Nepal': 'NPL',
             'Netherlands': 'NLD', 'Netherlands Antilles': 'ANT',
             'New Caledonia': 'NCL', 'New Zealand': 'NZL', 'Nicaragua': 'NIC',
             'Niger': 'NER', 'Nigeria': 'NGA', 'Norway': 'NOR', 'Oman': 'OMN',
             'Pakistan': 'PAK', 'Palau': 'PLW', 'Panama': 'PAN',
             'Papua New Guinea': 'PNG', 'Paraguay': 'PRY', 'Peru': 'PER',
             'Philippines': 'PHL', 'Poland': 'POL', 'Portugal': 'PRT',
             'Qatar': 'QAT', 'Réunion': 'REU', 'Romania': 'ROM',
             'Rwanda': 'RWA', 'Samoa': 'WSM', 'São Tomé & Príncipe': 'STP',
             'Saudi Arabia': 'SAU', 'Senegal': 'SEN', 'Serbia': 'SER',
             'Seychelles': 'SYC', 'Sierra Leone': 'SLE', 'Singapore': 'SIN',
             'Slovenia': 'SVN', 'Solomon Islands': 'SLB', 'Somalia': 'SOM',
             'South Africa': 'ZAF', 'Spain': 'ESP', 'Sri Lanka': 'LKA',
             'St. Kitts and Nevis': 'KNA', 'St. Lucia': 'LCA',
             'St. Vincent & Grens.': 'VCT', 'Sudan': 'SDN', 'Suriname': 'SUR',
             'Swaziland': 'SWZ', 'Sweden': 'SWE', 'Switzerland': 'CHE',
             'Syrian Arab Republic': 'SYR', 'Tajikistan': 'TJK',
             'Tanzania': 'TZA', 'Thailand': 'THA', 'Togo': 'TGO',
             'Tonga': 'TON', 'Trinidad & Tobago': 'TTO', 'Tunisia': 'TUN',
             'Turkey': 'TUR', 'Turkmenistan': 'TKM', 'Uganda': 'UGA',
             'Ukraine': 'UKR', 'United Arab Emirates': 'ARE',
             'Great Britain': 'GBR', 'United States': 'USA', 'Uruguay': 'URY',
             'Uzbekistan': 'UZB', 'Vanuatu': 'VUT', 'Venezuela': 'VEN',
             'Vietnam': 'VNM', 'West Bank/Gaza Strip': 'WBG',
             'Republic of Yemen': 'YEM', 'Yugoslavia': 'YUG', 'Zambia': 'ZMB',
             'Zimbabwe': 'ZWE'}
    # Had trouble with the following country codes:
    # 'North Korea':'PRK','Slovakia':'SVK','Cyprus':'CYP','Russia':'RUS',


fname = 'data.pkl'
if os.path.isfile(fname):
    pkl_file = open(fname, 'rb')
    medalsDF = pickle.load(pkl_file)
    pkl_file.close()
    # pprint.pprint(data2)

else:
    import requests
    # https://github.com/ekelleyv/medalbot
    r = requests.get('http://www.medalbot.com/api/v1/medals')
    if r.status_code == 200:
        medalsByCountry = r.json()

    medalsDF = pd.DataFrame(medalsByCountry)


    # GDP percentage
    
    import quandl

    # Read API key from EnvVar if exists
    quandl_api_key = os.getenv('QUANDLKEY', 'OR PLACE YOUR KEY KERE')
    quandl.ApiConfig.api_key = quandl_api_key

    col = np.empty(len(medalsDF['country_name']),)
    col[:] = np.nan
    medalsDF.loc[:, 'GDP'] = pd.Series(col, index=medalsDF.index)

    # for each country that earned >=1 medal,
    for name in medalsDF['country_name']:
        # look up the three-letter code for that country
        if name in codes:
            # Print for debugging
            print(name, codes[name])
            try:
                # Try to get the GDP on Quandl
                mydata = quandl.get("ODA/"+codes[name]+"_PPPSH",
                                    start_date="2016-01-01",
                                    end_date="2017-01-01")
                medalsDF.loc[(medalsDF.country_name == name),
                             'GDP'] = mydata['Value'][-1]
            except:
                print("Unexpected error:", sys.exc_info()[0])
        else:
            print('No code. Skipping', name)
    print(medalsDF.loc[:, 'GDP'].sort_values(ascending=False)[:5])

    # POPULATION
    medalsDF.loc[:, 'Population'] = pd.Series(col, index=medalsDF.index)
    for name in medalsDF['country_name']:
        if name in codes:
            print(name, codes[name])
            try:
                mydata = quandl.get("WORLDBANK/"+codes[name]+"_SP_POP_TOTL",
                                    start_date="2013-01-01",
                                    end_date="2017-01-01")
                medalsDF.loc[(medalsDF.country_name == name),
                             'Population'] = mydata['Value'][-1]
            except:
                print("Unexpected error:", sys.exc_info()[0])
        else:
            print('Skipping ' + name)

    print(medalsDF.loc[:, 'Population'].sort_values(ascending=False)[:5])

    # Save results
    output = open(fname, 'wb')
    # Pickle the list using the highest protocol available.
    pickle.dump(medalsDF, output, -1)
    output.close()
    # import pprint
    # pprint.pprint(data1)

# MAP

col = np.empty(len(medalsDF['country_name']),)
col[:] = np.nan
medalsDF.loc[:, 'code'] = pd.Series(col, index=medalsDF.index)

for name in medalsDF['country_name']:
    if name in codes:
        medalsDF.loc[(medalsDF.country_name == name),
                     'code'] = codes[name]

