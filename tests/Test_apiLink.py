from selenium import webdriver
from selenium.webdriver.common.by import    By
import requests
class Test_Api:

    def test_api(self):
        response = requests.get("https://automationexercise.com/api/productsList")
        body = response.json()
        print([item['name'] for item in body["products"]])
        assert response.status_code == 200,"Failed to Access"



