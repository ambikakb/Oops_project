import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
class TestNykaa:
    @pytest.fixture
    def d(self, request):
        d = webdriver.Chrome()
        d.maximize_window()
        d.implicitly_wait(30)
        d.get("https://www.nykaa.com/")
        request.addfinalizer(d.quit)
        return d
    def test_login(self, d):
        d.find_element(By.XPATH, "//button[@class='css-16vyron']").click()
        d.find_element(By.XPATH, "//button[@class='css-1yvfnuc']").click()
        email = d.find_element(By.NAME, "emailMobile")
        email.send_keys("ambikabkammar@gmail.com")
        d.find_element(By.XPATH, "//*[@type='submit']").click()
        password = d.find_element(By.NAME, "password")
        password.send_keys("Demo@#123")
        d.find_element(By.XPATH, "//button[@class='button big fill full small-button-seperator ']").click()
        expect='Ambika'
        element=d.find_element(By.XPATH, "//span[contains(@class,'css-17ukzrr euw1lbv4')]")
        assert expect in element.text






