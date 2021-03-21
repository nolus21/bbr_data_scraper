# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 00:22:11 2020

@author: nowak
"""
import pandas as pd

url_1 = 'https://dawa.aws.dk/adresser?q='
input_file = 'Pig_addresses.csv'




df = pd.read_csv(input_file, sep=';')

print(df)


for i,j,k,l in zip(df.StreetName, df.BuildingNumber, df.PostalCode, df.City):
    url_1_full = url_1 + i + ' ' + str(j) + ', ' + str(k) + ' ' + l
    print(url_1_full)