from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://knock.com.bd/product-category/anime/')
driver.maximize_window()

title_list = []  # You need to initialize this list before using it

for page in range(1,8):
    driver.get(f'https://knock.com.bd/product-category/anime/page/{page}/')

    #here {page} has been adjusted studying the pages of the knock website where the page number changes as /n/ not page = n
    
    for i in range(1,10):
        j = str(i)
        title = driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div/div[2]/div['+j+']/div/div[2]/div[2]/div[1]/p[2]/a').text 
        title_list.append(title)



    
print(title_list)

print(len(title_list))