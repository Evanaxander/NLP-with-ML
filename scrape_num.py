from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options to avoid detection
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

try:
    # Step 1: Search Google for "Laptop Shop Near Mirpur"
    driver.get('https://www.google.com')
    time.sleep(5)
    
    google_input = driver.find_element(By.NAME, 'q')
    google_input.send_keys("Laptop Shop Near Mirpur")
    google_input.send_keys(Keys.RETURN)
    time.sleep(5)
    
    # Step 2: Click on the Maps link
    try:
        # Try to find the Maps link using the full XPATH you provided
        maps_link = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[5]/div/div/div/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[2]/a/div')
        maps_link.click()
    except:
        # If that fails, try a more flexible approach
        maps_link = driver.find_element(By.XPATH, '//div[text()="Maps"]')
        maps_link.click()
    
    time.sleep(10)  # Wait for maps to load
    
    # Step 3: Scroll through the results and collect phone numbers
    phone_numbers = set()  # Using a set to avoid duplicates
    
    # Scroll multiple times to load more results
    for _ in range(20):
        # Scroll the sidebar
        scrollable_element = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]')
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_element)
        time.sleep(2)
        
        # Find all phone number elements
        phone_elements = driver.find_elements(By.XPATH, '//button[contains(@aria-label, "Phone")]')
        
        for element in phone_elements:
            try:
                # Click the phone button to reveal the number
                element.click()
                time.sleep(0.5)
                
                # The actual number is in a different element
                number_element = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]/div[7]/button/div/div[2]/div[1]')
                phone_number = number_element.text
                
                if phone_number and len(phone_number) >= 7:  # Basic validation
                    phone_numbers.add(phone_number)
                    print(f"Found phone number: {phone_number}")
                    
                    if len(phone_numbers) >= 100:
                        break
                
            except Exception as e:
                print(f"Error extracting phone number: {e}")
        
        if len(phone_numbers) >= 100:
            break
    
    print("\nCollected Phone Numbers:")
    for i, number in enumerate(phone_numbers, 1):
        print(f"{i}. {number}")

finally:
    driver.quit()