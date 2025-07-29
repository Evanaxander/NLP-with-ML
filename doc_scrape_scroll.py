from selenium import webdriver

from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()

driver.get('https://doctorola.com/')

driver.maximize_window()

driver.refresh()

height = driver.execute_script('return document.body.scrollHeight')

print(height)



for i in range(0,height+1200,60):
    driver.execute_script(f'window.scrollTo(0,{i});')
    time.sleep(0.5)

doc_info = driver.find_elements(By.XPATH,'//*[@id="search_result"]/a[2]').text

Doc_list = []
for i in comment:
    comment_list.append(i.text)

print(Doc_list)


time.sleep(20)



