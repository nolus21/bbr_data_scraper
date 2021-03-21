# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 16:35:00 2020

@author: nowak
"""






from selenium import webdriver
from time import sleep
import csv
import datetime

input_file = "Geocoded_101110_CVRudtræk_29.08.2020__Excel_FORARBEJDNING_AF_SVINEKOD_Virksomheder.csv"
outfile = "test_o"


def replace_delimiter():
    
    reader = csv.reader(open(input_file, newline=None), delimiter=',')  #WATCH OUT ON DELIMITER!
    writer = csv.writer(open(outfile, 'w'), delimiter=';')              #TAB delimited
    writer.writerows(reader)
        
replace_delimiter()


def printscreen(outfile):
    
    with open(outfile, encoding='utf-8-sig', newline='') as read_obj:
       
        csv_reader = csv.DictReader(read_obj, delimiter=';')
        print(csv_reader)
        
    

        
        
# =============================================================================
#         for row in csv_reader:
#             base = 'https://kort.degulesider.dk/?'
#             lat = row['Lat']
#             lon = row['Long']
#             fixed_lat = lat.replace(",",".")
#             fixed_lon = lon.replace(",",".")
#             zoom = '&z=17'
#             graphic = '&l=aerial'
#             #print(row)
#             url = base + 'c=' + fixed_lat + ',' + fixed_lon + zoom + graphic
#             #url = row['\ufeffurl']
#             print(url)
# =============================================================================
            
            
            url = 'https://www.google.com/maps'
            driver = webdriver.Chrome()
            driver.get(url)
            sleep(1)
    
            
            #WE WANT TO NOT AGREE (CHANGE IT) OR SCRAPER VIA vpn
            driver.find_elements_by_xpath('//*[@id="qc-cmp2-ui"]/div[2]/div/button')[0].click()
            driver.find_elements_by_xpath('//*[@id="page"]/div[16]/button')[0].click()
            sleep(1)
        #naming files according to DATE_TIME
            #date_stamp = str(datetime.datetime.now()).split('.')[0]
            #date_stamp = date_stamp.replace(" ", "_").replace(":", "_").replace("-", "_")
                    #naming files according to Excel
            title = row['FacilityName']
            file_name = title + ".png"
            
            
            
            driver.get_screenshot_as_file(file_name)
            
            driver.quit()
            print("end...")
                


printscreen(outfile)
#'https://kort.degulesider.dk/?c=55.488684,8.473232&z=17&l=aerial&q=%22arla%20foods%20amba%20esbjreg%20mejeri%22;yp'
