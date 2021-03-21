# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 13:41:21 2020

@author: nowak
"""
# -*- coding: utf-8 -*-

import pandas as pd
from geopy.geocoders import Nominatim
import numpy as np
import chardet


pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)





input_file = 'D:/DK_DATA_MASTER\DK\CVR_data/Direct_CVR_download/csv/014620_CVRudtræk_29.08.2020__Excel_PRODUKTION_AF_SLAGTESVIN_Virksomheder.csv'



def check_encoding():
    with open(input_file, 'rb') as rawdata:
        result = chardet.detect(rawdata.read(100000))
    print(result)
check_encoding()

#watch out to SAVE csv files as utf-8


def remove_x_from_column():
    df1 = pd.read_csv(input_file, encoding = 'utf-8-sig', sep = ';') #ISO-8859-1 #latin-1
    #print(df1)
    
    #checking types to cancat
    print(type(str(df1["Postnr."][0].item())))
    
    #concating to full address
    df1["Address_full_2"] = df1["Adresse"] + ", " + df1["Postnr."].astype(str) + " " + df1["By"]
    Address1 = df1["Address_full_2"]
    print(Address1)
    identified1 = df1['Address_full_2'].str.contains('c/o', regex=False)
    onlyAddress = Address1[identified1].str.split('-', expand=True) #change index...()
    # =============================================================================
    # print(onlyAddress[1])
    # print(onlyAddress.index)
    # print(type(onlyAddress))
    # print(pd.Series(onlyAddress[1]))
    # =============================================================================
     
    df1['Address_full_2'].update(onlyAddress[1])
    print(df1)
    print(df1['Address_full_2'])



# Nominatim Check!!!


    nom = Nominatim(user_agent="olostefaniak@gmail.com") # EMAIL ADDRESS TO USE
    
    df1["Coordinates"] = df1["Address_full_2"].apply(nom.geocode)
    
    df1["Lat"] = df1["Coordinates"].apply(lambda x: x.latitude if x != None else None)
    
    df1["Lon"] = df1["Coordinates"].apply(lambda x: x.longitude if x != None else None)
    
    print(df1["Lat"])
    
    df1.to_csv("Geocoded_014620_CVRudtræk_29.08.2020__Excel_PRODUKTION_AF_SLAGTESVIN_Virksomheder.csv", encoding = 'utf-8-sig', index=False)


remove_x_from_column()






