from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 1. Setup Headless Options
options = Options()
options.add_argument("--headless=new")  # Updated for modern Chrome
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# 2. Initialize Driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    # 3. Retry logic: Wait up to 10 seconds for the container to be ready
    print("Connecting to application...")
    for i in range(10):
        try:
            driver.get("http://127.0.0.1:5000")
            break
        except:
            time.sleep(1)

    # 4. Assertions
    assert "DevOps Assignment" in driver.page_source
    print("Homepage Test Passed")

except Exception as e:
    print(f"Test Failed: {e}")
    exit(1) # Ensure Jenkins sees the failure if it happens

finally:
    driver.quit()
