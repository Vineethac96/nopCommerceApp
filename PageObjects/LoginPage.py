from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

'''Here instaed of checking for visisble property, we are using locators and finding elemnts and performing actions on them'''

class LoginPage:

    '''Selenium locators - ID,Name,ClassName,tagName, Css selector,Xpath,Linktxt,Patial link text -QA'''
    textbox_username = "Email"
    textbox_password = "Password"
    btn_login = "//button[@type='submit']"
    link_logout = "Logout"

    '''constructor of the login page class'''
    def __init__(self,driver):  #constructor-used for initializing driver
        self.driver = driver

    '''this is to set username'''
    def setUsername(self,username):
        self.driver.find_element(By.ID, self.textbox_username).clear()   #good practice to clear field before inputing data
        self.driver.find_element(By.ID, self.textbox_username).send_keys(username)


    '''this is to set password'''
    def setPassword(self,password):
        self.driver.find_element(By.ID, self.textbox_password).clear()
        self.driver.find_element(By.ID,self.textbox_password).send_keys(password)


    '''this is used to login to app'''
    def do_login(self):
        self.driver.find_element(By.XPATH,self.btn_login).click()

    '''this is used to logout from app'''
    def do_logout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout).click()

