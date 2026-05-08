from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://YOUR_EC2_IP:5000")

assert driver.current_url == "http://YOUR_EC2_IP:5000/"

print("URL Test Passed")

driver.quit()
