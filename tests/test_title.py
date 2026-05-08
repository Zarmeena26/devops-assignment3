from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    driver.get("http://127.0.0.1:5000")
    time.sleep(2)
    
    # Check if 'DevOps' is in the page text (more reliable than URL)
    assert "DevOps" in driver.page_source
    print("URL/Title Test Passed")

except Exception as e:
    print(f"Test Failed: {e}")
    exit(1)
finally:
    driver.quit()
