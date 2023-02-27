from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:/Users/Devang/Downloads/chromedriver_win32 (1)/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com")

print(driver.title)
print(driver.current_url)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
print(driver.title)
print(driver.current_url)

driver.back()
print(driver.title)
print(driver.current_url)

driver.forward()
print(driver.title)
print(driver.current_url)

driver.refresh()
print(driver.title)
print(driver.current_url)

driver.close()