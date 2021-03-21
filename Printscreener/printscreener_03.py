from selenium import webdriver
from time import sleep
import csv
import datetime

input_file = "101110_cleaned_p-enheder.csv"
outfile = "test_facilities"


# =============================================================================
# def replace_delimiter():
#     
#     reader = csv.reader(open(input_file, newline=None), delimiter=',')  #WATCH OUT ON DELIMITER!
#     writer = csv.writer(open(outfile, 'w'), delimiter=';')              #TAB delimited
#     writer.writerows(reader)
#         
# replace_delimiter()
# =============================================================================

driver = webdriver.Chrome()
def printscreen(input_file):
    
    with open(input_file, encoding='ISO-8859-1', newline='') as read_obj:
       
        csv_reader = csv.DictReader(read_obj, delimiter=';')
        print(csv_reader)
        
    
        driver.get('https://kort.degulesider.dk/')
        sleep(3)
        driver.find_elements_by_xpath('//*[@id="qc-cmp2-ui"]/div[2]/div/button[1]')[0].click()
        sleep(1)
        
        for row in csv_reader:
            base = 'https://kort.degulesider.dk/?'
            lat = row['Lat']
            lon = row['Lon']
            fixed_lat = lat.replace(",",".")
            fixed_lon = lon.replace(",",".")
            zoom = '&z=17'
            graphic = '&l=aerial'
            #print(row)
            url = base + 'c=' + fixed_lat + ',' + fixed_lon + zoom + graphic
            #url = row['\ufeffurl']
            print(url)
            
            
            
            
            driver.get(url)
            sleep(1)
    
            
            #WE WANT TO NOT AGREE (CHANGE IT) OR SCRAPER VIA vpn
            
            driver.find_elements_by_xpath('//*[@id="page"]/div[16]/button')[0].click()
            
    
          #  driver.find_elements_by_xpath('//*[@id="qc-cmp2-ui"]/div[3]/div[2]/button[1]')[0].click()
            sleep(1)
        #naming files according to DATE_TIME
            #date_stamp = str(datetime.datetime.now()).split('.')[0]
            #date_stamp = date_stamp.replace(" ", "_").replace(":", "_").replace("-", "_")
                    #naming files according to Excel
            cvr = row['CVR']
            name = row['namePno']
            address = row['addressPno']
            city = row['cityPno']
            
            

            
            c_name = name.replace('/' ,'')
            c_address = address.replace('/' ,'')
            c_city = city.replace('/' ,'')
            
            file_name = cvr + '-' + c_name + '_' + c_address + '_' + c_city + ".png"
            
            
            
            driver.get_screenshot_as_file(file_name)
            
            #driver.quit()
            print("end...")
                


printscreen(input_file)
#'https://kort.degulesider.dk/?c=55.488684,8.473232&z=17&l=aerial&q=%22arla%20foods%20amba%20esbjreg%20mejeri%22;yp'
