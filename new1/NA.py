import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def login():
    d = webdriver.Edge()
    d.maximize_window()
    d.implicitly_wait(30)
    d.get("https://www.nykaa.com/")
    d.find_element(By.XPATH, "//button[@class='css-16vyron']").click()
    d.find_element(By.XPATH, "//button[@class='css-1yvfnuc']").click()
    d.find_element(By.NAME, "emailMobile").send_keys("ambikabkammar@gmail.com")
    d.find_element(By.XPATH, "//*[@type='submit']").click()
    d.find_element(By.NAME, "password").send_keys("Demo@#123")
    d.find_element(By.XPATH, "//button[@class='button big fill full small-button-seperator ']").click()
    time.sleep(5)
    return('Ambika')
    element = d.find_element(By.XPATH, "//span[contains(@class,'css-17ukzrr euw1lbv4')]")
def addingbag(self,d):
        d.find_element(By.XPATH, "//*[@name='search-suggestions-nykaa']").click()
        d.find_element(By.XPATH, "//*[@name='search-suggestions-nykaa']").send_keys("sweets")
        d.find_element(By.XPATH, "//*[@name='search-suggestions-nykaa']").send_keys(Keys.ENTER)
        d.find_element(By.XPATH, "//*[@alt='Nykaa Wanderlust Shower Gel']").click()
        for win in self.d.window_handles:
            d.switch_to.window(win)
            print(self.d.title)
            if d.title == "Nykaa Wanderlust Shower Gel":
                break
        element = self.d.find_element(By.XPATH, "//span[contains(text(),'Add to Bag')]")
        d.execute_script("arguments[0].click()", element)

def clickTosearch(self,d):
    try:
        d.find_element(By.XPATH, "//button[@class='css-16vyro']").click()
    except:
        return "Invalid xpath"


