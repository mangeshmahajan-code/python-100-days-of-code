from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import time,sleep

chrome_oprions =webdriver.ChromeOptions()
chrome_oprions.add_experimental_option("detach",True)

# selenium setup and open cookie clicker game
driver = webdriver.Chrome(options=chrome_oprions)
driver.get("https://ozh.github.io/cookieclicker/")
sleep(2)
eng_lang= driver.find_element(By.ID,value="langSelect-EN")
eng_lang.click()
sleep(2)

button = driver.find_element(By.ID,value="bigCookie")

wait_time = 5
timeout = time() + wait_time
five_min = time() + 60*5

# main loop to click cookie and buy items every 5 seconds, also prints cookie count and bought items
while True:
    button.click()

    if time()> timeout:
        try:
            cookies_element = driver.find_element(By.ID, value="cookies")  
            cookie_text = cookies_element.text
            cookie_count = int(cookie_text.split()[0].replace(",",""))
            print(f"cookie_count: {cookie_count}")

# find the most expensive item that can be bought and click it
            best_item = None
            for i in range(18,-1,-1):
                product = driver.find_element(by=By.ID, value=f"product{i}")
                
                if "product unlocked enabled" in product.get_attribute("class"):
                        best_item = product
                        break
                
            if best_item:
                best_item.click()
                      
                print(f"Bought item: {best_item.get_attribute('id')}")

        except(ValueError):
            print("Couldn't find cookie count or items")
        timeout= time()+ wait_time

# check if 5 minutes have passed, if so print final cookie count and break loop
    if time() > five_min:
            try:
                cookies_element = driver.find_element(by=By.ID, value="cookies")
                print(f"Final result: {cookies_element.text}")
            except ValueError:
                print("Couldn't get final cookie count")
            break
    