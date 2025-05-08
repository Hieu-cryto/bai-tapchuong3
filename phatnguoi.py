from selenium import webdriver
from selenium.webdriver.common.by import By
import requests as rq
from bs4 import BeautifulSoup as bf
import pandas as pd
import time

driver = webdriver.Chrome()

driver.get("https://phatnguoixe.com/")



click_xe_may = '#boxSearchForm > div > div > div.re__input-group--sm.re__search-box-row.js__search-row-location > div.re__listing-search-location-select-dropdown-position.js__listing-search-location-select-dropdown-position > div.re__city-search-select-dropdown.re__location-search-select-dropdown-container.js__city-search-select-dropdown.re__show-fade-in > div > div.re__city-search-select-list-wrapper > ul > li:nth-child(15) > span'    
element_xe_may = driver.find_element(By.CSS_SELECTOR, click_xe_may)
element_xe_may.click()

click_xe_may = '#btnSearch'    
element_xe_may = driver.find_element(By.CSS_SELECTOR, click_xe_may)
element_xe_may.click()


id_bien_so = 'bienso'
element_input = driver.find_element(By.ID, id_bien_so)
element_input.send_keys("92L103793")



# print(driver.title)

xpath_btn = '//*[@id="submit"]'
element_btn = driver.find_element(By.XPATH,xpath_btn)
element_btn.click()

time.sleep(10)
id_result = 'resultValue'
element_result = driver.find_element(By.ID, id_result)
text_result = element_result.text
if 'Không tìm thấy vi phạm phạt nguội!' in text_result:
    print('Không tìm thấy phạt nguội')
else:
    print('Tim thay phat nguoi')

input("Nhấn Enter để thoát...")