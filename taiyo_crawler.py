#!/usr/bin/env python
# coding: utf-8

# In[4]:


import csv
import pandas as pd
import random
import time
from parsel import Selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = Options()



chrome_options = webdriver.ChromeOptions()


driver = webdriver.Chrome(executable_path=r'chromedriver', options=chrome_options)

contract_urls = []
all_data = []
Nmes = []


for page in range(1,130):
    
    driver.get(f'https://www.contractsfinder.service.gov.uk/Search/Results?&page={page}')

    sleep(5)

    urls = driver.find_elements(By.XPATH, "//a[@class='govuk-link search-result-rwh break-word']")
    for url in urls:
        all_links = url.get_attribute("href")
        contract_urls.append(all_links)
        
        
        
for lnk in contract_urls:
    driver.get(lnk)
    sleep(5)
    name = driver.find_element(By.XPATH,"//h1[@class = 'govuk-heading-l break-word']")
    name_data = name.text
    Nmes.append(name_data)
    contract_details = driver.find_element(By.XPATH,'//div[@class="content-block"]')
    data_main= contract_details.text
    datas = data_main.split('\n')
    all_data.append(datas)
    print("[*] Saving Data...")
    
dtx = pd.DataFrame(all_data)
dtx['Name'] = Nmes

dtx.drop(dtx.columns[[0,1,3,5,7,9,11,13,15,17,19,21,23,24,26,29]] , axis = 1)
dtx.to_excel('Taiyo_scraper_data.xlsx')


# In[ ]:




