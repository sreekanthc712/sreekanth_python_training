from selenium import webdriver
from time import sleep
driver = webdriver.Chrome("./chromedriver")
driver.get("http://demowebshop.tricentis.com/")
sleep(2)
driver.find_element_by_xpath("//input[@value='Search']").click()
sleep(1)
print(driver.switch_to.alert.text)
sleep(2)
driver.switch_to.alert.accept()