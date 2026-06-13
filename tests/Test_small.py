import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_case:

    def test_name1(self):
        driver = webdriver.Chrome()
        driver.get("https://www.google.com/?zx=1759249531506&no_sw_cr=1")
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH,"//*[@class='gLFyf']").send_keys("testing")
        # time.sleep(10)
        # driver.find_element(By.XPATH,"//span[contains(text(),'testing')]/b[contains(text()=' browser']").click()
        # time.sleep(5)
        print("fine")