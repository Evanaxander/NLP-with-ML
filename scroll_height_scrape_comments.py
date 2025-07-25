from selenium import webdriver

from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()

driver.get('https://www.daraz.com.bd/products/-i345148524-s1687348589.html')

driver.maximize_window()

driver.refresh()

height = driver.execute_script('return document.body.scrollHeight')

print(height)



for i in range(0,height+1200,60):
    driver.execute_script(f'window.scrollTo(0,{i});')
    time.sleep(0.5)

comment = driver.find_elements(By.CLASS_NAME,'content')

comment_list = []
for i in comment:
    comment_list.append(i.text)

print(comment_list)


time.sleep(20)



