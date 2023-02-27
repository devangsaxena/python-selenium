import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:/Users/Devang/Downloads/chromedriver_win32 (1)/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")

productList=driver.find_elements(By.XPATH, "//div[@class='product']")
print(len(productList))
productPrice = 0
for product in productList:
    currentprice = int(product.find_element(By.XPATH, "p").text)
    productPrice += currentprice
    product.find_element(By.XPATH, "div/button").click()


driver.find_element(By.XPATH, "//a[@class='cart-icon']").click()

driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[@class='promoBtn']").click()
print(productPrice)
billPrice = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

print(billPrice)
time.sleep(10)
discountAmount=driver.find_element(By.CSS_SELECTOR, ".discountAmt").text

if billPrice == productPrice:
    print("Equal")
else:
    print("unequal")



print(discountAmount)

time.sleep(300)


