from selenium import webdriver

from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()

driver.get('https://www.batabd.com/collections/formal-shoes')

driver.maximize_window()

title = driver.find_element(By.XPATH, '//*[@id="shopify-section-collection-template-default"]/div/div[2]/div[2]/div/div/div[2]/a/span').text
link = driver.find_element(By.XPATH, '//*[@id="shopify-section-collection-template-default"]/div/div[2]/div[2]/div/div/div[2]/a/span').get_attribute('href')

print(title,link)

time.sleep(20)
