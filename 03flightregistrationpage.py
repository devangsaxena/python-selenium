import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:/Users/Devang/Downloads/chromedriver_win32 (1)/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/dropdownsPractise")
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countryList = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countryList))
for country in countryList:
    if country.text == "India":
        country.click()
        #print("India selected")
        break

print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))