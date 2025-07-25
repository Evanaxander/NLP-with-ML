#Scraping multiple data from daraz

#1 - XPATH with Loop
#2 - Class Name

#xpath: er index starts from 1  -> i
#index number = string
#typecast - int(i) -> str(i) a convert kore kaj korte during loop

#//*[@id="root"]/div/div[2]/div[i]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/a - relative xpath

# absolute - /html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/a


#step 1: Find out the pattern
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.daraz.pk/invisible-unisex-fashion-3/')
driver.maximize_window()

title_list = []  # You need to initialize this list before using it

for page in range(1,35):
    driver.get(f'https://www.daraz.pk/invisible-unisex-fashion-3/?page={page}')

    for i in range(1,41):
        j = str(i)
        title = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div['+j+']/div/div/div[2]/div[2]/a').text 
        title_list.append(title)



    
print(title_list)

print(len(title_list))
# page->all_products->page