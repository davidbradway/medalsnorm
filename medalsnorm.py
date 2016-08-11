# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 08:51:40 2016

@author: dpb6
"""


#MEDALS
import requests
#https://github.com/ekelleyv/medalbot
r = requests.get('http://www.medalbot.com/api/v1/medals')
if r.status_code == 200:
    medalsByCountry = r.json()

import pandas as pd
medalsDF = pd.DataFrame(medalsByCountry)


# Dict of country codes
codes = {'Afghanistan':'AFG',
'Albania':'ALB',
'Algeria':'DZA',
'American Samoa':'ASM',
'Angola':'AGO',
'Antigua and Barbuda':'ATG',
'Argentina':'ARG',
'Armenia':'ARM',
'Aruba':'ABW',
'Australia':'AUS',
'Austria':'AUT',
'Azerbaijan':'AZE',
'The Bahams':'BHS',
'Kingdom of Bahrain':'BHR',
'Bangladesh':'BGD',
'Barbados':'BRB',
'Belarus':'BLR',
'Belgium':'BEL',
'Belize':'BLZ',
'Benin':'BEN',
'Bermuda':'BMU',
'Bhutan':'BTN',
'Bolivia':'BOL',
'Bosnia & Herzegovina':'BIH',
'Botswana':'BWA',
'Brazil':'BRA',
'Brunei Darussalam':'BRN',
'Bulgaria':'BGR',
'Burkina Faso':'BFA',
'Burundi':'BDI',
'Cambodia':'KHM',
'Cameroon':'CMR',
'Canada':'CAN',
'Cape Verde':'CPV',
'Central African Rep.':'CAF',
'Chad':'TCD',
'Chile':'CHL',
'China':'CHN',
'People\'s Republic of China.:Hong Kong':'HKG',
'People\'s Republic of China.:Macao':'MAC',
'Colombia':'COL',
'Comoros':'COM',
'Democratic Republic of Congo':'ZAR',
'Republic of Congo':'COG',
'Costa Rica':'CRI',
'Côte d\'Ivoire':'CIV',
'Croatia':'HRV',
'Cuba':'CUB',
'Cyprus':'CYP',
'Czech Republic':'CZE',
'Denmark':'DNK',
'Djibouti':'DJI',
'Dominica':'DMA',
'Dominican Republic':'DOM',
'Ecuador':'ECU',
'Egypt':'EGY',
'El Salvador':'SLV',
'Equatorial Guinea':'GNQ',
'Eritrea':'ERI',
'Estonia':'EST',
'Ethiopia':'ETH',
'Faeroe Islands':'FRO',
'Fiji':'FJI',
'Finland':'FIN',
'France':'FRA',
'French Polynesia':'PYF',
'Gabon':'GAB',
'The Gambia':'GMB',
'Georgia':'GEO',
'Germany':'DEU',
'Ghana':'GHA',
'Gibraltar':'GIB',
'Greece':'GRC',
'Greenland':'GRL',
'Grenada':'GRD',
'Guadeloupe':'GLP',
'Guam':'GUM',
'Guatemala':'GTM',
'French Guiena':'GUF',
'Guinea':'GNB',
'Guinea-Bissau':'GIN',
'Guyana':'GUY',
'Haiti':'HTI',
'Honduras':'HND',
'Hungary':'HUN',
'Iceland':'ISL',
'India':'IND',
'Indonesia':'IDN',
'Islamic Republic of Iran':'IRN',
'Iraq':'IRQ',
'Ireland':'IRL',
'Israel':'ISR',
'Italy':'ITA',
'Jamaica':'JAM',
'Japan':'JPN',
'Jordan':'JOR',
'Kazakhstan':'KAZ',
'Kenya':'KEN',
'Kiribati':'KIR',
'South Korea':'KOR',
'Kuwait':'KWT',
'Kyrgyzstan':'KGZ',
'Lao People\'s Dem.Rep':'LAO',
'Latvia':'LVA',
'Lebanon':'LBN',
'Lesotho':'LSO',
'Liberia':'LBR',
'Libya':'LBY',
'Lithuania':'LTU',
'Luxembourg':'LUX',
'FYR Macedonia':'MKD',
'Madagascar':'MDG',
'Malawi':'MWI',
'Malaysia':'MYS',
'Maldives':'MDV',
'Mali':'MLI',
'Malta':'MLT',
'Martinique':'MTQ',
'Mauritania':'MRT',
'Mauritius':'MUS',
'Mexico':'MEX',
'Moldova':'MDA',
'Mongolia':'MNG',
'Morocco':'MAR',
'Mozambique':'MOZ',
'Myanmar':'MMR',
'Namibia':'NAM',
'Nauru':'NAU',
'Nepal':'NPL',
'Netherlands':'NLD',
'Netherlands Antilles':'ANT',
'New Caledonia':'NCL',
'New Zealand':'NZL',
'Nicaragua':'NIC',
'Niger':'NER',
'Nigeria':'NGA',
#'North Korea':'PRK',
'Norway':'NOR',
'Oman':'OMN',
'Pakistan':'PAK',
'Palau':'PLW',
'Panama':'PAN',
'Papua New Guinea':'PNG',
'Paraguay':'PRY',
'Peru':'PER',
'Philippines':'PHL',
'Poland':'POL',
'Portugal':'PRT',
'Qatar':'QAT',
'Réunion':'REU',
'Romania':'ROM',
'Russia':'RUS',
'Rwanda':'RWA',
'Samoa':'WSM',
'São Tomé & Príncipe':'STP',
'Saudi Arabia':'SAU',
'Senegal':'SEN',
'Serbia & Montenegro':'SER',
'Seychelles':'SYC',
'Sierra Leone':'SLE',
'Singapore':'SIN',
'Slovakia':'SVK',
'Slovenia':'SVN',
'Solomon Islands':'SLB',
'Somalia':'SOM',
'South Africa':'ZAF',
'Spain':'ESP',
'Sri Lanka':'LKA',
'St. Kitts and Nevis':'KNA',
'St. Lucia':'LCA',
'St. Vincent & Grens.':'VCT',
'Sudan':'SDN',
'Suriname':'SUR',
'Swaziland':'SWZ',
'Sweden':'SWE',
'Switzerland':'CHE',
'Syrian Arab Republic':'SYR',
'Tajikistan':'TJK',
'Tanzania':'TZA',
'Thailand':'THA',
'Togo':'TGO',
'Tonga':'TON',
'Trinidad and Tobago':'TTO',
'Tunisia':'TUN',
'Turkey':'TUR',
'Turkmenistan':'TKM',
'Uganda':'UGA',
'Ukraine':'UKR',
'United Arab Emirates':'ARE',
'Great Britain':'GBR',
'United States':'USA',
'Uruguay':'URY',
'Uzbekistan':'UZB',
'Vanuatu':'VUT',
'Bolivarian Republic of Venezuela':'VEN',
'Vietnam':'VNM',
'West Bank/Gaza Strip':'WBG',
'Republic of Yemen':'YEM',
'Yugoslavia':'YUG',
'Zambia':'ZMB',
'Zimbabwe':'ZWE'}


#GDP percentage
import quandl

# Read API key from EnvVar if exists
import os
quandl_api_key = os.getenv('QUANDLKEY','OR PLACE YOUR KEY KERE')
quandl.ApiConfig.api_key = quandl_api_key 

import sys

GDPbyName = {}
for name in medalsDF['country_name']:
    if name in codes:
        if name not in GDPbyName:
            print(codes[name])
            try:
                mydata = quandl.get("ODA/"+codes[name]+"_PPPSH", start_date="2016-01-01", end_date="2017-01-01")
                GDPbyName[name] = mydata['Value'][-1]
            except:
                print("Unexpected error:", sys.exc_info()[0])
    else:
        print('Skipping '+ name)

for w in sorted(GDPbyName, key=GDPbyName.get, reverse=True):
    print(w, GDPbyName[w])


# POPULATION
popByName = {}
for name in medalsDF['country_name']:
    if name in codes:
        if name not in popByName:
            print(codes[name])
            try:
                mydata = quandl.get("WORLDBANK/"+codes[name]+"_SP_POP_TOTL", start_date="2013-01-01", end_date="2017-01-01")
                popByName[name] = mydata['Value'][-1]
            except:
                print("Unexpected error:", sys.exc_info()[0])
    else:
        print('Skipping '+ name)

for w in sorted(popByName, key=popByName.get, reverse=True):
    print(w, popByName[w])

#MAP
'''
from kartograph import Kartograph
K = Kartograph()
K.generate(config, outfile='mymap.svg')
'''