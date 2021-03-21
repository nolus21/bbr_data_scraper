# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 10:30:28 2020

@author: nowak
"""


# import the geocoding services you'd like to try
from geopy.geocoders import ArcGIS, Bing, Nominatim, OpenCage, GoogleV3, OpenMapQuest #, GeocoderDotUS
import csv, sys
import pandas as pd

print ('creating geocoding objects!')

arcgis = ArcGIS(timeout=100)
bing = Bing('AsL7FxfxahbZIKcrKexOBUWvaPCBLrJYhQNJGb-qO8ApL65PKLSi40n-7Fc1yRWc',timeout=100)
nominatim = Nominatim(user_agent="olostefaniak@gmail.com", timeout=100)
#opencage = OpenCage('your-API-key',timeout=100)
#geocoderDotUS = GeocoderDotUS(timeout=100)
#googlev3 = GoogleV3(timeout=100) #since 2018 api key
#openmapquest = OpenMapQuest(timeout=100) #reqires api key

# choose and order your preference for geocoders here
geocoders = [nominatim, bing]

def geocode(Address1):
    i = 0
    try:
        while i < len(geocoders):
            # try to geocode using a service
            location = geocoders[i].geocode(address)

            # if it returns a location
            if location != None:
                
                # return those values
                return [location.latitude, location.longitude]
            else:
                # otherwise try the next one
                i += 1
    except:
        # catch whatever errors, likely timeout, and return null values
        print (sys.exc_info()[0])
        return ['null','null']

    # if all services have failed to geocode, return null values
    return ['null','null']

    
print ('geocoding addresses!')

# list to hold all rows
Lat = []
Lon = []

input_file = 'D:/DK_DATA_MASTER\DK\CVR_data/Direct_CVR_download/csv/014610_CVRudtræk_29.08.2020__Excel_AVL_af_SMAGRISE_Virksomheder.csv'

df1 = pd.read_csv(input_file, encoding = 'utf-8-sig', sep = ';') #ISO-8859-1 #latin-1
df1["Address_full_2"] = df1["Adresse"] + ", " + df1["Postnr."].astype(str) + " " + df1["By"] + ", Denmark"
Address1 = df1["Address_full_2"]

for key, value in Address1.iteritems():
    print(type(value)
    #print()
    


# =============================================================================
# with open(input_file, mode='r', encoding = 'utf-8-sig') as fin:
# 
#     reader = csv.reader(fin, delimiter=';')
#     next(reader) #SKIPPING HEADERS
#     j = 0
#     for row in reader:
#         print(row[1])
# =============================================================================
    print ('processing #',key)
    #j+=1
    try:
            # configure this based upon your input CSV file
# =============================================================================
#             street = row[4]
#             city = row[6]
#             state = row[7]
#             postalcode = row[5]
#             country = row[8]
#             address = street + ", " + city + ", " + state + " " + postalcode + " " + country
# =============================================================================
            
            
            
        result = geocode(value)
        print(result)
        # add the lat/lon values to the row
        #row.extend(result)
        # add the new row to master list
        Lat.append(str(result[0]))
        Lon.append(str(result[1]))
        
        
        
    except:
        print ('you are a beautiful unicorn')

print(Lat)    
print(Lon) 
df = pd.read_csv(input_file, sep=';')
for i,j in zip([Lat], [Lon]):
    df["Lat"] = i
    df["Lon"] = j
    
    df.to_csv("xxxxxGeocoded_univ_014610_CVRudtræk_29.08.2020__Excel_AVL_af_SMAGRISE_Virksomheder.csv", sep=';', encoding = 'utf-8-sig', index=False)

# =============================================================================
# print ('writing the results to file')
# print(dout)
# # print results to file
# with open('geocoded.csv', 'rt') as fout:
#     writer = csv.writer(fout)
#     writer.writerows(dout)
# =============================================================================

print ('all done!')

# ---------------------------------------------------------------------------------------------
# =============================================================================
# input_file = 'D:/DK_DATA_MASTER\DK\CVR_data/Direct_CVR_download/csv/101110_CVRudtræk_29.08.2020__Excel_FORARBEJDNING_AF_SVINEKOD_Virksomheder.csv'
# 
# df1 = pd.read_csv(input_file, encoding = 'utf-8-sig', sep = ';') #ISO-8859-1 #latin-1
# 
# 
# 
# #concating to full address
# df1["Address_full_2"] = df1["Adresse"] + ", " + df1["Postnr."].astype(str) + " " + df1["By"]
# Address1 = df1["Address_full_2"]
# print(Address1)
# 
# print(type(Address1))
# =============================================================================

# =============================================================================
# identified1 = df1['Address_full_2'].str.contains('c/o', regex=False)
# onlyAddress = Address1[identified1].str.split('-', expand=True) #change index...()
#  
# df1['Address_full_2'].update(onlyAddress[1])
# =============================================================================

#print(df1['Address_full_2'])
    
    
    
#GEOCODING ADDRESS
# =============================================================================
# result = geocode(Address1)
# print(result)
# =============================================================================
# =============================================================================
#     # add the lat/lon values to the row
#     row.extend(result)
#     # add the new row to master list
#     dout.append(row)
#     
#     
#     
# 
# print ('writing the results to file')
# 
# # print results to file
# with open('geocoded_by_UNIVERSAL.csv', 'wb') as fout:
#     writer = csv.writer(fout)
#     writer.writerows(dout)
# 
# print ('all done!')
# =============================================================================




# =============================================================================
# #checking types to cancat
# print(type(str(df1["Postnr."][0].item())))
# 
# #concating to full address
# df1["Address_full_2"] = df1["Adresse"] + ", " + df1["Postnr."].astype(str) + " " + df1["By"]
# address = df1["Address_full_2"]
# # -----------------------
# result = geocode(address)
# # add the lat/lon values to the row
# row.extend(result)
# # add the new row to master list
# dout.append(row)
# # print results to file
# with open('geocoded_by_UNIVERSAL.csv', 'wb') as fout:
#     writer = csv.writer(fout)
#     writer.writerows(dout)
# =============================================================================



