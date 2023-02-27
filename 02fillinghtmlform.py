import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:/Users/Devang/Downloads/chromedriver_win32 (1)/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME, "name").send_keys("abc")
driver.find_element(By.NAME, "email").send_keys("abc@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123")
driver.find_element(By.XPATH, "//input[@id='exampleCheck1']").click()
genderList = Select(driver.find_element(By.XPATH, "//select[@id='exampleFormControlSelect1']"))
genderList.select_by_index(1)
driver.find_element(By.XPATH, "//input[@value='option2']").click()
driver.find_element(By.XPATH, "//input[@name='bday']").send_keys("15031977")
driver.find_element(By.XPATH, "//input[@value='Submit']").click()
successmsg = driver.find_element(By.CLASS_NAME, "alert-success").text
if "Success" in successmsg:
    print("Registered Successfull")
else:
    print("Registration Unsuccess")


