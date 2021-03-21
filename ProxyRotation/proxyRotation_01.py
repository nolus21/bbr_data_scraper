# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 22:24:06 2020

@author: nowak
"""
import requests
from bs4 import BeautifulSoup
import json

res = requests.get('https://free-proxy-list.net')
#print(res.text)
content = BeautifulSoup(res.text, 'html.parser')
table = content.find('table')
rows = table.find_all('tr')
cols = [[col. text for col in row.find_all('td')] for row in rows]

proxies = []
proxy_index = 0


url = 'https://cvrapi.dk/api?search='
url_full = url + '84329819' + '&country=dk'

for col in cols:
    try:
        print(col)
        if col[4] == 'elite proxy' and col[6] == "yes" and col[3]== 'Netherlands':
            proxies.append('https://' + col[0] + ':' + col[1])
            
    except:
        pass
    
def fetch(url):
    global proxy_index
    while proxy_index < len(proxies):
        try:
            print('Trying proxy:', proxies[proxy_index])
            res = requests.get(url, proxies={'https': proxies[proxy_index]}, timeout=5)
            print(res)
            return res
        except:
            print('Bad proxy')
            proxy_index += 1
    
res = fetch(url_full)
print(res)



