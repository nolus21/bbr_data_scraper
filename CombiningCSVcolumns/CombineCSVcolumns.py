# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 14:06:07 2020

@author: nowak
"""

import pandas as pd


input_file1 = 'D:\\PIG_RESEARCH_WEBSITE\\Scripts\\CVRapi_scraper\\DONE\\101110\\CVR_info_CVRapi_scraping_result_for_101110_CVRudtræk_29.08.2020__Excel_FORARBEJDNING_AF_SVINEKOD_Virksomheder.csv'
input_file2 = 'D:\\DK_DATA_MASTER\\DK\\CVR_data\\Direct_CVR_download\\csv\\101110_CVRudtræk_29.08.2020__Excel_FORARBEJDNING_AF_SVINEKOD_Virksomheder.csv'

try:
    df1 = pd.read_csv(input_file1, sep = ';', encoding = 'utf-8-sig') #nrows=200,
    
    print(df1)
    
    df2 = pd.read_csv(input_file2, sep = ';', encoding = 'utf-8-sig') #nrows=200,
    print(df2)
    
    print(df2["Lat"])
    print(df2["Lon"])
    df3 = df1.join(df2["Lat"])
    df4 = df3.join(df2["Lon"])
    df4.to_csv('D:\\PIG_RESEARCH_WEBSITE\\Scripts\\CVRapi_scraper\\DONE\\014610\\GEOCODED_CVR_info_CVRapi_scraping_result_for_101110_CVRudtræk_29.08.2020__Excel_FORARBEJDNING_AF_SVINEKOD_Virksomheder.csv', 
               sep = ';', encoding = 'utf-8-sig')
    
except KeyError:
    print('key')