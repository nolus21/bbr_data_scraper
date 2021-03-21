# -*- coding: utf-8 -*-
import sys
import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
import unicodedata
import csv
import urllib3
import numpy as np
from urllib.request import urlopen
import urllib.request
from csv import writer
from csv import reader
import threading

def remove_diacritics(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str.replace('ł', 'l'))
    return u''.join([c for c in nfkd_form if not unicodedata.combining(c)])


input_file = 'Pig_addresses_from_Tablea_Ficilities_The_European_Pollutant_Release_and_Transfer_Register.csv'

url_1 = 'https://dawa.aws.dk/adresser?q=' #BASED ON CSV FILE !!! #Gjellerupvej%20105,%208220%20Brabrand
#fetch for id[0] to feed url_2
#fetch ejerlavkode to feed url_4
#fetch matrikelnr  to feed url_4
#fetch komkode  to feed url_3

#GET other
url_2 = 'https://dawa.aws.dk/bbrlight/enheder?adresseid=0a3f50bf-47cc-32b8-e044-0003ba298018'
#url_2 = 'https://dawa.aws.dk/adresser/' #b80001e9-cfe2-417c-981a-0605ea4f96ea
#fetch for ESREjdNr to feed url_3
#fetch for komkode to feed url_3

#GET

url_3 = 'https://dawa.aws.dk/bbrlight/bygninger?kommunekode='
#GET OPFOERELSE_AAR
#GET BYG_ARL_SAML
#GET other

url_4 = 'https://dawa.aws.dk/jordstykker?ejerlavkode='
#GET registreretareal
#GET vejareal




#url2 = 'https://dawa.aws.dk/bbrlight/bygninger?kommunekode=0101&esrejendomsnr='



# HERE ARRAYS FOR LAYERS TO SCRAPE:
addresseidArray = []                
matrikelnrArray = []
ejerlavkodeArray = []
komkodeArray = []
esrejendomsnrArray = []
adressebetegnelseArray = []
# FINAL SCRAPING FUNCTION
def get_addresseid_etc(input_file):

#fetch id to feed url_2
#fetch ejerlavkode to feed url_4
#fetch matrikelnr  to feed url_4
    
# =============================================================================
#     with open(input_file, encoding="utf8", newline='') as read_obj:
#         #spamreader = csv.reader(read_obj, delimiter=',', quotechar='|')    
#     
#         csv_reader = csv.DictReader(read_obj, delimiter=";")
#         #csv_writer = writer(write_obj)
#         #print(read_obj)
# =============================================================================
        
       
    try:
        df = pd.read_csv(input_file, sep=';')
        for i,j,k,l in zip(df.StreetName, df.BuildingNumber, df.PostalCode, df.City):
            print(type(j))
            print(type(k))
            print('CHECKING----------------------')
            if type(j) == float:
                j_str = str(int(j))
            elif type(j) == int:
                j_str = str(j)
            else:
                j_str = j
            #print(j_str)      
                
            if type(k) == float:
                k_str = str(int(k))
            elif type(k) == int:
                k_str = str(k)
            else:
                k_str = k
            #k_str = str(int(k))
            #print(k_str)
            
            url_1_full = url_1 + i + ' ' + j_str + ', ' + k_str + ' ' + l
            print(url_1_full)

            r = requests.get(url_1_full)
            #r.text
            soup = BeautifulSoup(r.text, 'html.parser')
            #print(r.text)
            json_data = json.loads(r.text)
# =============================================================================
#             print(json_data[0]['id'])
#             print(json_data[0]['adgangsadresse']['matrikelnr'])
#             print(json_data[0]['adgangsadresse']['ejerlav']['kode'])
#             print(json_data[0]['adgangsadresse']['kommune']['kode'])
#             print(json_data[0]['adgangsadresse']['esrejendomsnr']) 
# =============================================================================
            #addresseid
            if not json_data:
                 
                 addresseidArray.extend(['0'])
                 matrikelnrArray.extend(['0'])
                 ejerlavkodeArray.extend(['0'])
                 komkodeArray.extend(['0'])
                 esrejendomsnrArray.extend(['0'])
                 adressebetegnelseArray.extend(['0'])
            else: 
                addresseidArray.extend([json_data[0]['id']])
                matrikelnrArray.extend([json_data[0]['adgangsadresse']['matrikelnr']])
                ejerlavkodeArray.extend([json_data[0]['adgangsadresse']['ejerlav']['kode']])
                komkodeArray.extend([json_data[0]['adgangsadresse']['kommune']['kode']])
                esrejendomsnrArray.extend([json_data[0]['adgangsadresse']['esrejendomsnr']])
                adressebetegnelseArray.extend([json_data[0]['adressebetegnelse']])
                
    except KeyError:
        pass
    
    print(addresseidArray)
    print(matrikelnrArray)
    print(ejerlavkodeArray)
    print(komkodeArray)
    print(esrejendomsnrArray)
    print(adressebetegnelseArray)

get_addresseid_etc(input_file)


# =============================================================================
# ESREjdNrArray = []
# 
# def get_more_1():
# 
# #fetch for ESREjdNr to feed url_3
#     
#     try:
#         for i in addresseidArray:
#             url_2_full = url_2 + i
#             print(url_2_full)
#             
#             r = requests.get(url_2_full)
#             soup = BeautifulSoup(r.text, 'html.parser')
#             json_data = json.loads(r.text)
#             #print(json_data[0]['bygning']['ESREjdNr'])
#             
#             if not json_data:
#                      
#                 ESREjdNrArray.extend(['no data'])
#                
#             else: 
#                 ESREjdNrArray.extend([json_data[0]['bygning']['ESREjdNr']])
#                
#             
#             #print(json_data)
#             
#     except KeyError:
#         pass
#     
#     print(ESREjdNrArray)
#     
# get_more_1()
# =============================================================================





url_3_Array = []
OPFOERELSE_AARArray = []
BYG_ARL_SAMLArray = []
ESREjdNrArray = []


#url_3 = 'https://dawa.aws.dk/bbrlight/bygninger?kommunekode=' '0751&esrejendomsnr=133030'
def get_more_2():
    
    try:
        for i,j in zip(komkodeArray, esrejendomsnrArray): #zip means iteration through 2 lists at ONCE!!
            
            if j is not None:
                url_3_full = url_3 + i + '&esrejendomsnr=' + j
            else:
                url_3_fill = url_3 + i + '&esrejendomsnr=' + '0'
            print(i)
            print(j)
            print(url_3_full)
            #url_3_aArray.append(url_3_a)
            
            r = requests.get(url_3_full)
            soup = BeautifulSoup(r.text, 'html.parser')
            json_data = json.loads(r.text)
            
            if not json_data:
                     OPFOERELSE_AARArray.extend(['0'])
                     BYG_ARL_SAMLArray.extend(['0'])
                     ESREjdNrArray.extend(['0'])
   
            else: 
                for i in json_data:
                    
                    OPFOERELSE_AAR = i['OPFOERELSE_AAR']
                    BYG_ARL_SAML = i['BYG_ARL_SAML']
                    ESREjdNr = i['ESREjdNr']
                    
                    url_3_Array.extend([url_3_full])
                    
                    OPFOERELSE_AARArray.extend([OPFOERELSE_AAR])
                    BYG_ARL_SAMLArray.extend([BYG_ARL_SAML])
                    ESREjdNrArray.extend([ESREjdNr])
            

    except KeyError:
        pass
    
    #print(url_3_aArray)
    print(OPFOERELSE_AARArray)
    print(BYG_ARL_SAMLArray)
    print(url_3_Array)
    
get_more_2()


#-------------------------------------------------------------------------------------------------------


#GET registreretareal
#GET vejareal

registreretarealArray = []

def get_more_from_matrikelkortet():
    
    
    try:
        for i,j in zip(ejerlavkodeArray, matrikelnrArray):
            url_4_full = url_4 + str(i) + '&matrikelnr=' + j
            print(url_4_full)
            
            r = requests.get(url_4_full)
            soup = BeautifulSoup(r.text, 'html.parser')
            json_data = json.loads(r.text)
            
            if not json_data:
                registreretarealArray.extend(['0'])
                
            else:
                for i in json_data:
                    registreretareal = i['registreretareal']
                    
                    registreretarealArray.extend([registreretareal])
                    
    except KeyError:
        pass
    
    print(registreretarealArray)
    
get_more_from_matrikelkortet()


                
# =============================================================================
# def save_to_csv():
#    
#     
# # =============================================================================
# # addresseidArray = []                
# # matrikelnrArray = []
# # ejerlavkodeArray = []
# # komkodeArray = []
# # ESREjdNrArray = []
# # OPFOERELSE_AARArray = []
# # BYG_ARL_SAMLArray = []
# # registreretarealArray = []
# # =============================================================================
# 
# # =============================================================================
# #     
# #     df = pd.read_csv(input_file)
# #     df = pd.read_csv(input_file, sep=';') #use correct delimiter !!
# #     print(df.FacilityID)
# #     
# #     
# #     
# #     data = np.array(
# #         [["url", "addresseid", "matrikelnr", "ejerlavkode", "komkode", "ESREjdNr", "OPFOERELSE_AAR", "BYG_ARL_SAML", "registreretareal" ],
# #          urlArray, addresseidArray, matrikelnrArray, ejerlavkodeArray, komkodeArray, ESREjdNrArray, OPFOERELSE_AARArray, BYG_ARL_SAMLArray, registreretarealArray])
# #     
# #     df = pd.DataFrame(i for i in data).transpose()
# #     df.drop(0, axis=1, inplace=True)
# #     df.columns = data[0]
# #     print(df)
# #     
# #     df.to_csv("FINALFINAL.csv", index=False)
# # =============================================================================
#     
#     
#    
# =============================================================================

def save_to_csv_1():

    df = pd.read_csv(input_file, sep=';')
    for i,j,k,l,m,p in zip([addresseidArray], [matrikelnrArray], [ejerlavkodeArray], [komkodeArray], [esrejendomsnrArray], [registreretarealArray]):
        #[OPFOERELSE_AARArray], [BYG_ARL_SAMLArray]
        
        df["addresseid"] = i
        df["matrikelnr"] = j
        df["ejerlavkode"] = k
        df["komkode"] = l
        df["ESREjdNr"] = m
        #df["OPFOERELSE_AAR"] = n # -------add n to for     YOU COULD DO AVARAGE?
        #df["BYG_ARL_SAML"] = o # -------add o to for       YOU COULD DO SUM?
        df["registreretareal_plot"] = p
        
        
      
        
        df.to_csv('Pig_extended_01.csv', sep=';', index=False)
     
save_to_csv_1()

def save_to_csv_BUILDING_SPECIFIC():
    
    data = np.array(
        [["url", "OPFOERELSE_AAR", "BYG_ARL_SAML", "ESREjdNr"],
         url_3_Array, OPFOERELSE_AARArray, BYG_ARL_SAMLArray, ESREjdNrArray])
    
    df = pd.DataFrame(i for i in data).transpose()
    
    df.drop(0, axis=1, inplace=True)
    df.columns = data[0]
    print(df)
    
    df.to_csv("More_data.csv", index=False)
    
    
save_to_csv_BUILDING_SPECIFIC()



# =============================================================================
# data = np.array(
#     [["url", "Latitude", "Longitude", "OPFOERELSE_AAR", "BYG_ARL_SAML" ],
#      urlArray, latArray, lonArray, OPFOERELSE_AARArray, BYG_ARL_SAMLArray])
# 
# df = pd.DataFrame(i for i in data).transpose()
# df.drop(0, axis=1, inplace=True)
# df.columns = data[0]
# print(df)
# 
# df.to_csv("FINALFINAL.csv", index=False)
# =============================================================================





# =============================================================================
# df = pd.DataFrame({"url" : data[:, 0], "Latitude" : data[:, 1], "Longitude" : lonArray1[:, 2]})
# df.to_csv("FINALFINAL.csv", index=False)
# 
# print(df)
# =============================================================================




# =============================================================================
# df = pd.read_csv(cleaned_file)
# 
# # LONGITUDE & LATITUDE
# 
# for item in [urlArray]:
#     df["url"] = item
#     df.to_csv(cleaned_file, index=False)
# 
# 
# for item in [latArray]:
#     df["Latitude"] = item
#     df.to_csv(cleaned_file, index=False)
#     
# for item in [lonArray]:
#     df["Longitude"] = item
#     df.to_csv(cleaned_file, index=False)
# =============================================================================
# =============================================================================
#     
# # ois_ids
# for item in [ois_id_plotArray]:
#     df["ois_id_plot"] = item
#     df.to_csv(cleaned_file, index=False)
#     
# for item in [ois_id_buildingArray]:
#     df["ois_id_building"] = item
#     df.to_csv(cleaned_file, index=False)
#     
#     
# # OTHER DATA
# for item in [AntLejMKoekkenArray]:
#     df["AntLejMKoekken"] = item
#     df.to_csv(cleaned_file, index=False)
# 
# for item in [AntLejUKoekkenArray]:
#     df["AntLejUKoekken"] = item
#     df.to_csv(cleaned_file, index=False)
# 
# for item in [OPFOERELSE_AARArray]:
#     df["OPFOERELSE_AAR"] = item
#     df.to_csv(cleaned_file, index=False)
# 
# for item in [OMBYG_AARArray]:
#     df["OMBYG_AAR"] = item
#     df.to_csv(cleaned_file, index=False)
# 
# for item in [BYG_ARL_SAMLArray]:
#     df["BYG_ARL_SAML"] = item
#     df.to_csv(cleaned_file, index=False)
# 
# for item in [BYH_BOLIG_ARL_SAMLArray]:
#     df["BYH_BOLIG_ARL_SAML"] = item
#     df.to_csv(cleaned_file, index=False)
# 
# for item in [BYG_BEBYG_ARLArray]:
#     df["BYG_BEBYG_ARL"] = item
#     df.to_csv(cleaned_file, index=False)
# 
# for item in [KomKodeArray]:
#     df["KomKode"] = item
#     df.to_csv(cleaned_file, index=False)
# 
# for item in [LandsejerlavkodeArray]:
#     df["Landsejerlavkode"] = item
#     df.to_csv(cleaned_file, index=False)
# 
# =============================================================================

            

# =============================================================================
# df = df.loc[df['ESREjdNr'] == 'no data']
# df.to_csv("output.csv", index=False)
# =============================================================================
#nodata = input('no data')
# =============================================================================
# for row in df:#reading lines of csv
#     print(row)
#     for field in row:
#         print(field)
# =============================================================================
# =============================================================================
#     LeaveOnlyValid.append(row)
#     print(LeaveOnlyValid)
#     for field in row:
#         print(field)
# =============================================================================
# =============================================================================
#         if field == nodata:
#             print(field)
#             LeaveOnlyValid.remove(row)
#             df.to_csv(input_file, index=False)
# =============================================================================
            
    
# =============================================================================
#     if df["ESREjdNr"] == "no data":
#         df.to_csv(input_file, index=False)
# =============================================================================
    
#IF 'no data' REMOVE ROWS of csv



# =============================================================================
# # Read File
# csv_input = pd.read_csv("d:\python programs\chairs.csv")
# 
# # Remove duplicates
# csv_input = csv_input.drop_duplicates(subset=['Name'])
# =============================================================================
# =============================================================================
# df = pd.read_csv(input_file)
# # Remove records with price under 50
# df =  df[df['ESREjdNr'] == 'no data']
# =============================================================================

# =============================================================================
# # Create Quality Column
# csv_input["Quality"] = np.where(csv_input['Price']>125, 'High', 'Average')
# =============================================================================

# Save to CSV    
#df.to_csv(input_file, index=False)

       
    
# =============================================================================
# for item in [all_lon]:
#     df["Lon"] = item
#     df.to_csv(input_file, index=False)
# =============================================================================
    


#creating a list of new urls

# =============================================================================
# new_urls = [url2 + x for x in ESREnumbers]
# print(new_urls)
# 
# df = pd.read_csv(input_file)
# for item in [new_urls]:
#     df["new_urls"] = item
#     df.to_csv(input_file, index=False)
# =============================================================================
    







# =============================================================================
# def further_data_gathering_based_BUILDINGS(input_file, output_file):
#     
#         try:
#             for url3 in new_urls:
#                 #print(url3)
#                 r = requests.get(url3)
#                 soup = BeautifulSoup(r.text, 'html.parser')
#                 #print(r.text)
#                 
#                 json_data = json.loads(r.text)
# # =============================================================================
# #                 readable_json = json.dumps(json_data)
# #                 ESRE = readable_json[0]['ESREjdNr']
# #                 for i in ESRE:
# #                     print (i['ESREjdNr'])
# # =============================================================================
#                 
#                 for i in json_data:
#                     coordinates = i['bygningspunkt']["koordinater"]
#                     print (coordinates)
#                     
# # =============================================================================
# #                     ESREnumbers.extend([ESREnu])
# #                     print(ESREnumbers)
# # =============================================================================
#          
#         except KeyError:
#             print(" nie wyszlo cos w drugim")
#             
#      
# further_data_gathering_based_BUILDINGS(input_file, output_file)   
# =============================================================================













    










        