from selenium import webdriver
from time import sleep
# from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.monsterindia.com/")
sleep(1)
driver.find_element_by_name("fts").send_keys("python")
sleep(1)
driver.find_element_by_xpath("(//strong[text()='python'])[1]").click()