from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 1. Setup Headless Options for EC2
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# 2. Initialize Driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    # 3. Give the container a few seconds to wake up
    time.sleep(3)
    driver.get("http://127.0.0.1:5000")

    # 4. Assertions
    # Note: Using 127.0.0.1 is more stable in Jenkins than 'localhost'
    assert driver.current_url == "http://127.0.0"
    print("URL Test Passed")

except Exception as e:
    print(f"Test Failed: {e}")
    exit(1)
finally:
    driver.quit()
