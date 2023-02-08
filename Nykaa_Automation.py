import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Nykaa:
    def __init__(self):
        self.d = webdriver.Edge()
        self.d.maximize_window()
        self.d.implicitly_wait(30)
        self.d.get("https://www.nykaa.com/")

    def login(self):
        self.d.find_element(By.XPATH, "//button[@class='css-16vyron']").click()
        self.d.find_element(By.XPATH, "//button[@class='css-1yvfnuc']").click()
        self.d.find_element(By.NAME, "emailMobile").send_keys("ambikabkammar@gmail.com")
        self.d.find_element(By.XPATH, "//*[@type='submit']").click()
        self.d.find_element(By.NAME, "password").send_keys("Demo@#123")
        self.d.find_element(By.XPATH, "//button[@class='button big fill full small-button-seperator ']").click()
        expect = 'Ambika'
        element = self.d.find_element(By.XPATH, "//span[contains(@class,'css-17ukzrr euw1lbv4')]")

    def addingbag(self):
        return 0

class Addbag(Nykaa):
    def addingbag(self):
        self.d.find_element(By.XPATH, "//*[@name='search-suggestions-nykaa']").click()
        self.d.find_element(By.XPATH, "//*[@name='search-suggestions-nykaa']").send_keys("sweets")
        self.d.find_element(By.XPATH, "//*[@name='search-suggestions-nykaa']").send_keys(Keys.ENTER)
        self.d.find_element(By.XPATH, "//*[@alt='Nykaa Wanderlust Shower Gel']").click()
        for win in self.d.window_handles:
            self.d.switch_to.window(win)
            print(self.d.title)
            if self.d.title == "Nykaa Wanderlust Shower Gel":
                break
        element = self.d.find_element(By.XPATH, "//span[contains(text(),'Add to Bag')]")
        self.d.execute_script("arguments[0].click()", element)


    def add_address(self):

        self.d.find_element(By.XPATH, "//button[@type='button' and @class='css-g4vs13']").click()
        self.d.switch_to.frame(self.d.find_element(By.XPATH, "//iframe[@src='/mobileCartIframe?ptype=customIframeCart']"))
        time.sleep(5)
        self.d.find_element(By.XPATH, "//span[@class=' css-1l4d0ex e171rb9k3']").click()
        time.sleep(5)
        self.d.find_element(By.XPATH, "//p[text()='Add New Address']").click()
        self.d.find_element(By.XPATH, "//*[@placeholder='Pincode']").send_keys("577427")
        self.d.find_element(By.XPATH, "//*[@placeholder='House/ Flat/ Office No.']").send_keys("House") #Some time this field will not accept the Input
        self.d.find_element(By.XPATH, "//*[@placeholder='Road Name/ Area /Colony']").send_keys("kammar") #Some time this field will not accept the Input
        self.d.find_element(By.XPATH, "//*[@placeholder='Name']").send_keys("Ambika")
        self.d.find_element(By.XPATH, "//*[@placeholder='Phone']").send_keys("9764578723")
        self.d.find_element(By.XPATH, "//button[text()='Ship to this address']").click()

    def clickTosearch(self):
        try:
            self.d.find_element(By.XPATH, "//button[@class='css-16vyro']").click()
        except:
            print("Invalid xpath")


#Menu driven
obj = Addbag()
while True:
    print("Enter 1 for login")
    print("Enter 2 for Add Items to Bag")
    print("Enter 3 to Add address, if the items are already added in the Bag of logged in user")
    print("Enter 4 for clickToSearch")
    print("Enter 5 to exit")
    userchoice = int(input())
    if userchoice == 1:
        obj.login()
    elif userchoice == 2:
        obj.addingbag()
    elif userchoice == 3:
        obj.add_address()
    elif userchoice == 4:
        obj.clickTosearch()
    elif userchoice == 5:
        quit()















