import pytest
import time
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import LoginPage  #we need to login as well
from PageObjects.addCustomerPage import AddCustomer
from Utilities.customLogger import LogGen
from Configurations.config import TestData
import string
import random # we use this class for random generation of mail id


# to generate random mail id-QA
def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


class Test_003_AddCustomer:



    logger = LogGen.loggen()  # Logger


    @pytest.mark.sanity
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_addCustomer(self,setup):
        self.logger.info("************* Test_003_AddCustomer **********")
        self.driver=setup
        self.driver.get(TestData.BaseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)   # using login class to do login

        self.lp.setUsername(TestData.Username)
        self.lp.setPassword(TestData.Password)
        self.lp.do_login()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Add Customer Test **********")

        self.addcust = AddCustomer(self.driver)   #creating object of addCustomer Class

        self.addcust.clickOnCustomersMenu()
        #self.addcust.clickOnCustomersMenuItem()
        self.addcust.clickOnAddnew()

        self.logger.info("************* Providing customer info **********")

        self.email = random_generator() + "@gmail.com" #dynamic: data-generate random mail id for everytime we run test instaed of one single hardcoded value everytime
        self.addcust.setEmail(self.email)   #removed hardcoded value here

        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Pavan")
        self.addcust.setLastName("Kumar")
        self.addcust.setDob("7/05/1985")  # Format: D / MM / YYY
        self.addcust.setCompanyName("busyQA")
        self.addcust.setAdminContent("This is for testing.........")
        self.addcust.clickOnSave()

        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add customer validation started *****************")

        #TEST - valdating by checking id "customer has been added successfully is displayed"

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text   #get entire tag names on the page body
        print(self.msg)   #list all the msg's
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")

