import requests
import json
import urllib3
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import numpy as np

from selenium import webdriver
from time import sleep
import csv
import datetime
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from selenium.webdriver.chrome.options import Options

#CVR based search - perhaps some of the companies do also SIDE ACTIVITIES
# EXTEND CVR INFORMATION BY THESE FIELDS
vatCvrArr = []
nameCvrArr = []
addressCvrArr = []
zipcodeCvrArr = []
cityCvrArr = []
citynameCvrArr = []
protectedCvrArr = []
phoneCvrArr = []
emailCvrArr = []
startdateCvrArr = []
enddateCvrArr = []
employeesCvrArr = []
companycodeCvrArr = []
companydescCvrArr = []
creditstartdateCvrArr = []
creditbankruptCvrArr = []
creditstatusCvrArr = []
ownersNameCvrArr = []

# THIS IS A SPETIAL ARRAY contining CVR numbers multiplied by the amount of p-enheder
vatCvrEXTENDEDArray = []
#------------------------
## EXTEND PNO INFORMATION BY THESE FIELDS - ADD TO CVR LIST ALL THE RELEVANT


pnoPnoArr = []
mainPnoArr = []
namePnoArr = []
addressPnoArr = []
zipcodePnoArr = []
cityPnoArr = []
protectedPnoArr = []
phonePnoArr = []
emailPnoArr = []
startdatePnoArr = []
enddatePnoArr = []
employeesPnoArr = []
addresscoPnoArr = []
industrycodePnoArr = []
industrydescPnoArr = []

#------------------------

input_file = '014620_CVRudtræk_29.08.2020__Excel_PRODUKTION_AF_SLAGTESVIN_Virksomheder.csv'

url = 'https://cvrapi.dk/api?search='
driver = webdriver.Chrome()

chrome_options = Options()
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless")
# chrome_options.headless = True # also works
driver = webdriver.Chrome(options=chrome_options)
#start_url = "https://duckgo.com"
#driver.get(start_url)
#print(driver.page_source.encode("utf-8"))
#driver.quit()
# b'<!DOCTYPE html><html xmlns="http://www....


# =============================================================================
# binary = FirefoxBinary('C:\geckodriver')
# driver = webdriver.Firefox(firefox_binary=binary)
# =============================================================================






def cvrapi2():
    
    try:
        df = pd.read_csv(input_file, sep = ';', nrows=200, encoding = 'utf-8-sig') #nrows=200,
        
        for i in (df['CVR-nummer']):
            
            cvr = str(i)
            global url_full
            #cvr = str(1008535716)
            url_full = url + cvr + '&country=dk'
            
            #print(url_full)
        
        #old scraping with bsoup
# =============================================================================
#             html = urlopen(url_full)
#             soup = BeautifulSoup(html, 'html.parser')
#            
#             json_data=json.loads(str(soup)) #quite special case where soup IS json
#             print(json_data)
# =============================================================================
            
            
            
            driver.get(url_full)
            sleep(0.5)
    
            #WE WANT TO NOT AGREE (CHANGE IT) OR SCRAPER VIA vpn
            result = driver.find_element_by_tag_name('pre').text
            #print(result)
            #sleep(1)
            
            json_data = json.loads(result)
            #print(json_data["vat"])
            
            #driver.quit()
            #print("end...")
            
            #--------CVR - Virksomheder data section------------
            vatCvrArr.extend([json_data["vat"]])
            nameCvrArr.extend([json_data["name"]])
            addressCvrArr.extend([json_data["address"]])
            zipcodeCvrArr.extend([json_data["zipcode"]])
            cityCvrArr.extend([json_data["city"]])
            citynameCvrArr.extend([json_data["cityname"]])
            protectedCvrArr.extend([json_data["protected"]])
            phoneCvrArr.extend([json_data["phone"]])
            emailCvrArr.extend([json_data["email"]])
            startdateCvrArr.extend([json_data["startdate"]])
            enddateCvrArr.extend([json_data["enddate"]])
            employeesCvrArr.extend([json_data["employees"]])
            companycodeCvrArr.extend([json_data["companycode"]])
            companydescCvrArr.extend([json_data["companydesc"]])
            creditstartdateCvrArr.extend([json_data["creditstartdate"]])
            creditbankruptCvrArr.extend([json_data["creditbankrupt"]])
            creditstatusCvrArr.extend([json_data["creditstatus"]])
            ownersNameCvrArr.extend([json_data["owners"]])
            
            print(json_data["vat"])
            
# =============================================================================
#             print(nameCvrArr)
#             print(addressCvrArr)
#             print(zipcodeCvrArr)
#             print(citynameCvrArr)
#             print(protectedCvrArr)
#             print(phoneCvrArr)
#             print(emailCvrArr)
#             print(startdateCvrArr)
#             print(enddateCvrArr)
#             print(employeesCvrArr)
#             print(companycodeCvrArr)
#             print(companydescCvrArr)
#             print(creditstartdateCvrArr)
#             print(creditbankruptCvrArr)
#             print(creditstatusCvrArr)
#             print(ownersNameCvrArr)
# =============================================================================
            
            #---------P-enheder - productionunits section--------
            for k in json_data['productionunits']:
                
                
                pnoPnoArr.extend([k["pno"]])
                mainPnoArr.extend([k["main"]])
                namePnoArr.extend([k["name"]])
                addressPnoArr.extend([k["address"]])
                zipcodePnoArr.extend([k["zipcode"]])
                cityPnoArr.extend([k["city"]])
                protectedPnoArr.extend([k["protected"]])
                phonePnoArr.extend([k["phone"]])
                emailPnoArr.extend([k["email"]])
                startdatePnoArr.extend([k["startdate"]])
                enddatePnoArr.extend([k["enddate"]])
                employeesPnoArr.extend([k["employees"]])
                addresscoPnoArr.extend([k["addressco"]])
                industrycodePnoArr.extend([k["industrycode"]])
                industrydescPnoArr.extend([k["industrydesc"]])
                
            for m in json_data['productionunits']:
                vatCvrEXTENDEDArray.extend([json_data["vat"]])
                #print(vatCvrEXTENDEDArray)
                
# =============================================================================
#         LatCvrArr.extend(df['Lat'])
#         LonCvrArr.extend(df['Lon'])
#             
#         print(LonCvrArr)
# =============================================================================
            
    except KeyError:
        print('NOT THIS TIME')
         
                
cvrapi2()   

#---------------------------------
         



output_file = 'CVRapi_scraping_result.csv' 
def save_to_csv_1():
    
    df = pd.DataFrame()
    #df = pd.read_csv(output_file, sep=';')
    for g,h,i,j,k,l,m,n,o,p,r,s,t,u,w,x,y,z in zip([vatCvrArr],
                     [nameCvrArr],#
                     [addressCvrArr],#
                     [zipcodeCvrArr],#
                     [cityCvrArr],#
                     [citynameCvrArr],#
                     [protectedCvrArr],#
                     [phoneCvrArr],#
                     [emailCvrArr],#
                     [startdateCvrArr],#
                     [enddateCvrArr],#
                     [employeesCvrArr],#
                     [companycodeCvrArr],#
                     [companydescCvrArr],#
                     [creditstartdateCvrArr],#
                     [creditbankruptCvrArr],#
                     [creditstatusCvrArr],#
                     [ownersNameCvrArr]
                     ):
        
        df["CVR"] = g
        df["nameCvr"] = h
        df["addressCvr"] = i
        df["zipcodeCvr"] = j
        df["cityCvr"] = k
        df["citynameCvr"] = l
        df["protectedCvr"] = m
        df["phoneCvr"] = n
        df["emailCvr"] = o
        df["startdateCvr"] = p
        df["enddateCvr"] = r
        df["employeesCvr"] = s
        df["companycodeCvr"] = t
        df["companydescCvr"] = u
        df["creditstartdateCvr"] = w
        df["creditbankruptCvr"] = x
        df["creditstatusCvr"] = y
        df["ownersNameCvr"] = z
        
# =============================================================================
#     for a, b, c, d, e, f, in zip ([pnoPnoArr],
#                                   [mainPnoArr],
#                                   [namePnoArr],
#                                   [addressPnoArr],
#                                   [zipcodePnoArr],
#                                   [cityPnoArr],
#                                   [protectedPnoArr],
#                                   [phonePnoArr],
#                                   [emailPnoArr],
#                                   [startdatePnoArr],
#                                   [enddatePnoArr],
#                                   [employeesPnoArr],
#                                   [addresscoPnoArr],
#                                   [industrycodePnoArr],
#                                   [industrydescPnoArr],
#                                   ):
#         df["P-nummer"] = g
#         df["mainPno"] = h
#         df["namePno"] = i
#         df["addressPno"] = j
#         df["zipcodePno"] = k
#         df["cityPno"] = l
#         df["protectedPno"] = m
#         df["phonePno"] = n
#         df["emailPno"] = o
#         df["startdatePno"] = p
#         df["enddatePno"] = r
#         df["employeesPno"] = s
#         df["addresscoPno"] = t
#         df["industrycodePno"] = u
#         df["industrydescPno"] = w
# =============================================================================
      
     
        df.to_csv('04_014620_CVRudtræk_29.08.2020__Excel_PRODUKTION_AF_SLAGTESVIN_Virksomheder.csv', sep=';', index=False, encoding = 'utf-8-sig')

save_to_csv_1()


def save_to_csv_BUILDING_SPECIFIC():
    

    data = np.array(
        [["CVR",
          "P-nummer",
          "mainPno",
          "namePno",
          "addressPno",
          "zipcodePno",
          "cityPno",
          "protectedPno",
          "phonePno",
          "emailPno",
          "startdatePno",
          "enddatePno",
          "employeesPno",
          "addresscoPno",
          "industrycodePno",
          "industrydescPno"],
         vatCvrEXTENDEDArray,
         pnoPnoArr, 
         mainPnoArr, 
         namePnoArr, 
         addressPnoArr,
         zipcodePnoArr,
         cityPnoArr,
         protectedPnoArr,
         phonePnoArr,
         emailPnoArr,
         startdatePnoArr,
         enddatePnoArr,
         employeesPnoArr,
         addresscoPnoArr,
         industrycodePnoArr,
         industrydescPnoArr])
    
    df = pd.DataFrame(i for i in data).transpose()
    
    df.drop(0, axis=1, inplace=True)
    df.columns = data[0]
    #print(df)
    
    df.to_csv("04_P-enheder_info_CVRapi_scraping_result_for_014620_CVRudtræk_29.08.2020__Excel_PRODUKTION_AF_SLAGTESVIN_Virksomheder.csv", sep=';', index=False, encoding = 'utf-8-sig')

    
save_to_csv_BUILDING_SPECIFIC()
        
        
        

        



# =============================================================================
# {
#   "vat": 18731231,
#   "name": "LANDMAND JENS BUSK HENDRIKSEN",
#   "address": "Højvangsvej 6",
#   "zipcode": "8870",
#   "city": "Langå",
#   "cityname": null,
#   "protected": false,
#   "phone": "86461346",
#   "email": null,
#   "fax": null,
#   "startdate": "01/07 - 1995",
#   "enddate": null,
#   "employees": 0,
#   "addressco": null,
#   "industrycode": 14620,
#   "industrydesc": "Produktion af slagtesvin",
#   "companycode": 10,
#   "companydesc": "Enkeltmandsvirksomhed",
#   "creditstartdate": null,
#   "creditbankrupt": false,
#   "creditstatus": null,
#   "owners": [
#     {
#       "name": "Jens Busk Hendriksen"
#     }
#   ],
#   "productionunits": [
#     {
#       "pno": 1003539586,
#       "main": true,
#       "name": "LANDMAND JENS BUSK HENDRIKSEN",
#       "address": "Højvangsvej 6",
#       "zipcode": "8870",
#       "city": "Langå",
#       "cityname": null,
#       "protected": false,
#       "phone": "86461346",
#       "email": null,
#       "fax": null,
#       "startdate": "01/07 - 1995",
#       "enddate": null,
#       "employees": "2-4",
#       "addressco": null,
#       "industrycode": 14620,
#       "industrydesc": "Produktion af slagtesvin"
#     }
#   ],
#   "t": 100,
#   "version": 6
# }
# =============================================================================

#Write your company name + project name in useragent when you make the posting
#You must write a useragent string that tells your company name and possibly. 
#a project name - name and contact number would be a good idea. Can look like this: 
#'CVR API - CRM system - Martin Mikkelsen +45 42424242' or 'CVR API - Front page lookup' - ie: 
#'[your company name - [your project name] - [contact person's name] [contact person's phone or e -mail] '