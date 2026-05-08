from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://YOUR_EC2_IP:5000")

assert "DevOps Assignment" in driver.page_source

print("Homepage Test Passed")

driver.quit()
